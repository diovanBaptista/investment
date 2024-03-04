import { Module } from '@nestjs/common';
import { InvestmentService } from './investment.service';
import { InvestmentController } from './investment.controller';
import { TypeOrmModule } from '@nestjs/typeorm';
import { Investment } from './entities/investment.entity';
import { AuthModule } from 'src/auth/auth.module';
import { EmailModule } from 'src/email/email.module';
import { UserModule } from 'src/user/user.module';

@Module({
  controllers: [InvestmentController],
  providers: [InvestmentService],
  imports: [
    TypeOrmModule.forFeature([Investment]),
    AuthModule,
    EmailModule,
    UserModule,
  ],
})
export class InvestmentModule {}
