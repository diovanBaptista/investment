import { PartialType } from '@nestjs/mapped-types';
import { CreateInvestmentDto } from './create-investment.dto';
import { ApiProperty } from '@nestjs/swagger';

export class UpdateInvestmentDto extends PartialType(CreateInvestmentDto) {
  @ApiProperty({
    description: 'The investment status',
    type: Boolean,
  })
  withdraw: boolean;

  @ApiProperty({
    description: 'The withdraw date of the investment',
    type: Date,
  })
  withdraw_at: Date;
}
