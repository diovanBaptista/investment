import { Injectable } from '@nestjs/common';
import { CreateUserDto } from './dto/create-user.dto';
import { UpdateUserDto } from './dto/update-user.dto';
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
    const newUser = this.userRepository.create(createUserDto);
    return this.userRepository.save(newUser);
  }

  findAll() {
    return this.userRepository.find({
      select: ['id', 'username'],
    });
  }

  findOneByUsername(username: string) {
    return this.userRepository.findOne({
      where: [{ username }],
    });
  }

  findOne(id: string) {
    return this.userRepository.findOne({
      where: [{ id }],
    });
  }
}
