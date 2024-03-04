import {
  Controller,
  Get,
  Post,
  Body,
  Param,
  BadRequestException,
} from '@nestjs/common';
import { UserService } from './user.service';
import { CreateUserDto } from './dto/create-user.dto';
import { HashPasswordPipe } from '../common/pipes/hash-password.pipe';
import { ApiBody, ApiOperation, ApiTags } from '@nestjs/swagger';

@Controller('user')
@ApiTags('user')
export class UserController {
  constructor(private readonly userService: UserService) {}

  @Post()
  @ApiOperation({ summary: 'Creation new user' })
  @ApiBody({ type: CreateUserDto })
  async create(
    @Body() createUserDto: CreateUserDto,
    @Body('password', HashPasswordPipe) passwordHashed: string,
  ) {
    const userExists = await this.userService.findOneByUsernameOrEmail(
      createUserDto.username,
      createUserDto.email,
    );
    if (userExists) {
      throw new BadRequestException('User already exists');
    }
    const userCreated = await this.userService.create({
      ...createUserDto,
      password: passwordHashed,
    });

    return userCreated;
  }

  @Get()
  @ApiOperation({ summary: 'Find all users list' })
  findAll() {
    return this.userService.findAll();
  }

  @Get(':id')
  @ApiOperation({ summary: 'Find one user by ID' })
  findOne(@Param('id') id: string) {
    return this.userService.findOne(id);
  }
}
