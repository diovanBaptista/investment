import {
  Controller,
  Get,
  Post,
  Body,
  Patch,
  Param,
  Delete,
  Query,
  UseGuards,
  Req,
  NotFoundException,
  BadRequestException,
} from '@nestjs/common';
import { InvestmentService } from './investment.service';
import { CreateInvestmentDto } from './dto/create-investment.dto';
import { UpdateInvestmentDto } from './dto/update-investment.dto';
import {
  ApiBearerAuth,
  ApiBody,
  ApiOperation,
  ApiQuery,
  ApiTags,
} from '@nestjs/swagger';
import { AuthGuard } from 'src/auth/auth.guard';
import { AuthService } from 'src/auth/auth.service';
import { differenceInMonths } from 'date-fns';

@Controller('investment')
@ApiTags('investment')
@UseGuards(AuthGuard)
@ApiBearerAuth()
export class InvestmentController {
  constructor(
    private readonly investmentService: InvestmentService,
    private authService: AuthService,
  ) {}

  @Post()
  @ApiOperation({ summary: 'Create new investment' })
  @ApiBody({ type: CreateInvestmentDto })
  create(
    @Body() createInvestmentDto: CreateInvestmentDto,
    @Req() request: Request,
  ) {
    const authorizationHeader = request.headers['authorization'];
    const getUserId = this.authService.getUserIdFromToken(authorizationHeader);

    const payload = {
      user: getUserId,
      ...createInvestmentDto,
    };

    return this.investmentService.create(payload);
  }

  @Get()
  @ApiOperation({ summary: 'Get all investments' })
  @ApiQuery({
    name: 'page',
    description: 'Page number',
    required: false,
    type: Number,
  })
  @ApiQuery({
    name: 'limit',
    description: 'Number of items per page',
    required: false,
    type: Number,
  })
  findAll(
    @Query('page') page: number = 1,
    @Query('limit') limit: number = 10,
    @Req() request: Request,
  ) {
    // the user can see their investments
    const authorizationHeader = request.headers['authorization'];
    const getUserId = this.authService.getUserIdFromToken(authorizationHeader);

    return this.investmentService.findAll({ page, limit }, getUserId);
  }

  @Get(':id')
  @ApiOperation({ summary: 'Get investment by ID' })
  async findOne(@Param('id') id: string) {
    try {
      const investment = await this.investmentService.findOne(id);

      if (!investment) {
        throw new NotFoundException('Investment not found');
      }

      const currentDate = new Date();
      const createdAtDate = new Date(investment.created_at);

      const monthsPassed = differenceInMonths(currentDate, createdAtDate);

      const gainPercentage = 0.052;
      const gainPerMounth = monthsPassed * gainPercentage * investment.value;

      const expectedValue = Number(
        (gainPerMounth + Number(investment.value)).toFixed(2),
      );

      const payload = {
        ...investment,
        expected_value: expectedValue,
      };
      return payload;
    } catch (error) {
      throw error;
    }
  }

  @Patch(':id')
  @ApiOperation({ summary: 'Update investment and withdraw by ID' })
  async update(
    @Param('id') id: string,
    @Body() updateInvestmentDto: UpdateInvestmentDto,
  ) {
    try {
      const investment = await this.investmentService.findOne(id);

      if (!investment) {
        throw new NotFoundException('Investment not found');
      }

      if (investment.withdraw && updateInvestmentDto.withdraw) {
        // the investment can only be withdrawn once
        throw new BadRequestException('Investment already withdrawn');
      }

      const withdrawAtDate = new Date(updateInvestmentDto.withdraw_at);
      const createdAtDate = new Date(investment.created_at);
      const dateNow = new Date();

      if (
        withdrawAtDate.getTime() <= createdAtDate.getTime() ||
        withdrawAtDate.getTime() >= dateNow.getTime()
      ) {
        throw new BadRequestException(
          'The investment cannot be withdrawn on that date',
        );
      }
    } catch (error) {
      throw error;
    }
    return this.investmentService.update(id, updateInvestmentDto);
  }

  @Delete(':id')
  @ApiOperation({ summary: 'Delete investment by ID' })
  remove(@Param('id') id: string) {
    return this.investmentService.remove(+id);
  }
}
