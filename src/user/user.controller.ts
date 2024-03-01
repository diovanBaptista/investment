import { Controller, Get, Post, Body, Param, UsePipes } from '@nestjs/common';
import { UserService } from './user.service';
import { CreateUserDto } from './dto/create-user.dto';
import { User } from './entities/user.entity';
import { HashPasswordPipe } from '../common/pipes/hash-password.pipe';

@Controller('user')
export class UserController {
  constructor(private readonly userService: UserService) {}

  @Post()
  async create(
    @Body() createUserDto: CreateUserDto,
    @Body('password', HashPasswordPipe) passwordHashed: string,
  ) {
    console.log(passwordHashed);
    const userCreated = await this.userService.create({
      ...createUserDto,
      password: passwordHashed,
    });

    return userCreated;
  }

  @Get()
  findAll() {
    return this.userService.findAll();
  }

  @Get(':id')
  findOne(@Param('id') id: string) {
    return this.userService.findOne(id);
  }
}
