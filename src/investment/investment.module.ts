import { Module } from '@nestjs/common';
import { InvestmentService } from './investment.service';
import { InvestmentController } from './investment.controller';
import { TypeOrmModule } from '@nestjs/typeorm';
import { Investment } from './entities/investment.entity';

@Module({
  controllers: [InvestmentController],
  providers: [InvestmentService],
  imports: [TypeOrmModule.forFeature([Investment])],
})
export class InvestmentModule {}
