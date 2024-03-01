import { ApiProperty } from '@nestjs/swagger';
import { IsEmail, IsString } from 'class-validator';

export class CreateUserDto {
  @IsString()
  @ApiProperty({
    description: 'Name of user',
  })
  username: string;

  @IsEmail()
  @ApiProperty({
    description: 'Email of user',
    format: 'email',
  })
  email: string;

  @IsString()
  @ApiProperty({
    description: 'Password of user',
  })
  password: string;
}
