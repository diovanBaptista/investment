import { ApiProperty } from '@nestjs/swagger';
import { IsString } from 'class-validator';

export class SignInDto {
  @IsString()
  @ApiProperty({
    description: 'Name of user',
  })
  username: string;

  @IsString()
  @ApiProperty({
    description: 'Password of user',
  })
  password: string;
}
