import { Injectable } from '@nestjs/common';
import { CreateUserDto } from './dto/create-user.dto';
import { InjectRepository } from '@nestjs/typeorm';
import { User } from './entities/user.entity';
import { Repository } from 'typeorm';

@Injectable()
export class UserService {
  constructor(
    @InjectRepository(User)
    private readonly userRepository: Repository<User>,
  ) {}

  create(createUserDto: CreateUserDto) {
    const user = this.userRepository.create(createUserDto);
    return this.userRepository.save(user);
  }

  findAll() {
    return this.userRepository.find({
      select: ['id', 'username', 'email'],
    });
  }

  findOneByUsername(username: string) {
    return this.userRepository.findOne({
      where: [{ username: username }, { email: username }],
    });
  }

  findOneByUsernameOrEmail(username: string, email: string) {
    return this.userRepository.findOne({
      where: [{ username: username }, { email: email }],
    });
  }

  findOne(id: string) {
    return this.userRepository.findOne({
      where: [{ id }],
    });
  }
}
