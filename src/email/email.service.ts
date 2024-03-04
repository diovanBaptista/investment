// email.service.ts

import { MailerService } from '@nestjs-modules/mailer';
import { Injectable } from '@nestjs/common';
import { User } from './../user/entities/user.entity';
import { Investment } from 'src/investment/entities/investment.entity';
import * as path from 'path'; // Import the path module

@Injectable()
export class EmailService {
  constructor(private mailerService: MailerService) {}

  async sendInvestmentConfirmation(user: User, investment: Investment) {
    const htmlContent = `
      <p>Hey ${user.username},</p>
      <p>
        Your investment has been confirmed successfully!
      </p>
      <p>
        Amount invested : ${investment.value},
      </p>
      <p>Coderockr investments, thanks you.</p>
    `;

    await this.mailerService.sendMail({
      to: user.email,
      subject: 'Investment created successfully',
      html: htmlContent,
    });
  }
}
