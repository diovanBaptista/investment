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
  @ApiOperation({
    summary: 'Create new investment',
  })
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
    const authorizationHeader = request.headers['authorization'];
    const getUserId = this.authService.getUserIdFromToken(authorizationHeader);
    return this.investmentService.findAll({ page, limit }, getUserId);
  }

  @Get(':id')
  @ApiOperation({ summary: 'Get investment by ID' })
  findOne(@Param('id') id: string) {
    return this.investmentService.findOne(+id);
  }

  @Patch(':id')
  @ApiOperation({ summary: 'Update investment by ID' })
  update(
    @Param('id') id: string,
    @Body() updateInvestmentDto: UpdateInvestmentDto,
  ) {
    return this.investmentService.update(+id, updateInvestmentDto);
  }

  @Delete(':id')
  @ApiOperation({ summary: 'Delete investment by ID' })
  remove(@Param('id') id: string) {
    return this.investmentService.remove(+id);
  }
}
