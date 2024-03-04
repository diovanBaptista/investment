import { Injectable } from '@nestjs/common';

@Injectable()
export class AppService {
  getHello(): string {
    return '#rockr_lovers!🖤 See documentation in http://localhost:8000/api#/';
  }
}
