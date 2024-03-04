import { JwtService } from '@nestjs/jwt';
import { UserService } from './../user/user.service';
import { SignInDto } from './dto/sign-in.dto';
import { Injectable, UnauthorizedException } from '@nestjs/common';
import * as bcrypt from 'bcrypt';

@Injectable()
export class AuthService {
  constructor(
    private userService: UserService,
    private jwtService: JwtService,
  ) {}

  async signIn(signInDto: SignInDto): Promise<any> {
    const user = await this.userService.findOneByUsername(signInDto.username);

    const userIsAuthenticated = await bcrypt.compare(
      signInDto.password,
      user.password,
    );

    if (!userIsAuthenticated) {
      throw new UnauthorizedException();
    }

    const payload = {
      sub: user.id,
      email: user.email,
    };

    const accessToken = await this.jwtService.signAsync(payload);
    return {
      access_token: accessToken,
    };
  }

  getUserIdFromToken(accessToken: string): string {
    try {
      const token = accessToken.split(' ')[1];
      const decodedToken: any = this.jwtService.verify(token); // Usamos o método verify do JwtService para decodificar o token

      const userId: string = decodedToken.sub;
      return userId;
    } catch (error) {
      return null;
    }
  }
}
