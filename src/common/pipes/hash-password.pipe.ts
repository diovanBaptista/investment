import { BadRequestException, Injectable, PipeTransform } from '@nestjs/common';
import * as bcrypt from 'bcrypt';
import { CreateUserDto } from '../../user/dto/create-user.dto';

@Injectable()
export class HashPasswordPipe implements PipeTransform {
  async transform(password: string) {
    try {
      const salt = process.env.SALT_PASSWORD;

      const passwordHash = await bcrypt.hash(password, salt);

      return passwordHash;
    } catch (error) {
      throw new BadRequestException('Erro ao transformar a senha.');
    }
  }
}
