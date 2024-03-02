import { Injectable } from '@nestjs/common';
import { CreateInvestmentDto } from './dto/create-investment.dto';
import { UpdateInvestmentDto } from './dto/update-investment.dto';
import { InjectRepository } from '@nestjs/typeorm';
import { Investment } from './entities/investment.entity';
import { Repository } from 'typeorm';

@Injectable()
export class InvestmentService {
  constructor(
    @InjectRepository(Investment)
    private readonly investmentRepository: Repository<Investment>,
  ) {}
  create(createInvestmentDto: CreateInvestmentDto) {
    const investment = this.investmentRepository.create(createInvestmentDto);
    return this.investmentRepository.save(investment);
  }

  findAll({ page = 1, limit = 10 }, userId: string) {
    const offset = (page - 1) * limit;
    return this.investmentRepository.find({
      where: {
        user: { id: userId },
      },
      skip: offset,
      take: limit,
      order: {
        updated_at: 'DESC',
      },
    });
  }

  findOne(id: string) {
    return this.investmentRepository.findOne({
      where: { id },
    });
  }

  update(id: number, updateInvestmentDto: UpdateInvestmentDto) {
    return `This action updates a #${id} investment`;
  }

  remove(id: number) {
    return `This action removes a #${id} investment`;
  }
}
