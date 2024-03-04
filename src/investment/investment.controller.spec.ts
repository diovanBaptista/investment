import { Test, TestingModule } from '@nestjs/testing';
import { InvestmentController } from './investment.controller';
import { InvestmentService } from './investment.service';
import { Investment } from './entities/investment.entity';
import { Repository } from 'typeorm';
import { getRepositoryToken } from '@nestjs/typeorm';

describe('InvestmentController', () => {
  let controller: InvestmentController;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      controllers: [InvestmentController],
      providers: [
        InvestmentService,
        {
          provide: getRepositoryToken(Investment),
          useClass: Repository,
        },
      ],
    }).compile();

    controller = module.get<InvestmentController>(InvestmentController);
  });

  it('should be defined', () => {
    expect(controller).toBeDefined();
  });
});
