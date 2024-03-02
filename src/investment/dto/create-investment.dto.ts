import { ApiProperty } from '@nestjs/swagger';
import {
  IsNotEmpty,
  IsNumber,
  IsOptional,
  IsPositive,
  Validate,
} from 'class-validator';
import { DateNowOrPastValidator } from 'src/common/validators/date-now-or-past.validator';
import { User } from 'src/user/entities/user.entity';

export class CreateInvestmentDto {
  @IsNumber({ maxDecimalPlaces: 2 })
  @IsPositive()
  @ApiProperty({
    description: 'Investment value',
    type: Number,
    example: 998.98,
  })
  value: number;

  @IsOptional()
  user: User;

  @IsOptional()
  @Validate(DateNowOrPastValidator)
  @ApiProperty({
    description: 'The creation date of the entity',
    example: '2024-03-01T12:00:00Z',
    type: Date,
  })
  created_at: Date;
}
