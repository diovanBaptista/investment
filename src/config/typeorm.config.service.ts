import { Injectable } from '@nestjs/common';
import { ConfigService } from '@nestjs/config';
import { TypeOrmModuleOptions, TypeOrmOptionsFactory } from '@nestjs/typeorm';
import { join } from 'node:path';

@Injectable()
export class TypeOrmConfigService implements TypeOrmOptionsFactory {
  constructor(private configService: ConfigService) {}

  createTypeOrmOptions(): TypeOrmModuleOptions {
    return {
      type: 'postgres',
      host: this.configService.get<string>('DATABASE_HOST'),
      port: +this.configService.get<string>('DATABASE_PORT'),
      username: this.configService.get<string>('DATABASE_USER'),
      password: this.configService.get<string>('DATABASE_PASS'),
      database: this.configService.get<string>('DATABASE_NAME'),
      entities: [join(__dirname, '/../**/**.entity{.ts,.js}')],
      autoLoadEntities: true,
      synchronize: true,
    };
  }
}
