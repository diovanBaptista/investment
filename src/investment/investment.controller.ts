import {
  Controller,
  Get,
  Post,
  Body,
  Patch,
  Param,
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
import { EmailService } from 'src/email/email.service';
import { UserService } from 'src/user/user.service';

@Controller('investment')
@ApiTags('investment')
@UseGuards(AuthGuard)
@ApiBearerAuth()
export class InvestmentController {
  constructor(
    private readonly investmentService: InvestmentService,
    private authService: AuthService,
    private emailService: EmailService,
    private userService: UserService,
  ) {}

  @Post()
  @ApiOperation({ summary: 'Create new investment' })
  @ApiBody({ type: CreateInvestmentDto })
  async ddddddcreate(
    @Body() createInvestmentDto: CreateInvestmentDto,
    @Req() request: Request,
  ) {
    const authorizationHeader = request.headers['authorization'];
    const getUserId = this.authService.getUserIdFromToken(authorizationHeader);

    const payload = {
      user: getUserId,
      ...createInvestmentDto,
    };

    const investment = await this.investmentService.create(payload);
    const findUser = await this.userService.findOne(getUserId);
    await this.emailService.sendInvestmentConfirmation(findUser, investment);
    return investment;
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
  @ApiOperation({
    summary: 'Get investment by ID',
    description: 'Get investment details and balance',
  })
  async findOne(@Param('id') id: string) {
    try {
      const investment = await this.investmentService.findOne(id);

      if (!investment) {
        throw new NotFoundException('Investment not found');
      }

      const currentDate = new Date();
      const createdAtDate = new Date(investment.created_at);

      // calculate difference between mouths
      const monthsPassed = differenceInMonths(currentDate, createdAtDate);

      const gainPercentage = 0.0052;
      const gainPerMounth = gainPercentage * investment.value;

      const expectedValue = Number(
        (gainPerMounth * monthsPassed + Number(investment.value)).toFixed(2),
      );

      const payload = {
        ...investment,
        expected_value: expectedValue,
      };

      // calculation withdraw tax
      if (investment.withdraw) {
        let tax = 0;

        /**
         * Discount value example
         * investment = 1000
         * expectedValue = 1200
         * discountValue == 200
         * the discount will be applied to the amount generated
         */
        const discountValue = expectedValue - investment.value;
        if (monthsPassed < 12) {
          tax = 0.225;
        } else if (monthsPassed >= 12 && monthsPassed < 24) {
          tax = 0.185;
        } else {
          tax = 0.15;
        }

        const amountBalance = expectedValue - discountValue * tax;
        payload['balance'] = Number(amountBalance.toFixed(2));
      }

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

      if (
        (investment.withdraw && updateInvestmentDto.withdraw) ||
        investment.withdraw_at
      ) {
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
}
