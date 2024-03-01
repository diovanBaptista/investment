import { ApiProperty } from '@nestjs/swagger';
import {
  Column,
  CreateDateColumn,
  Entity,
  PrimaryGeneratedColumn,
  UpdateDateColumn,
} from 'typeorm';

@Entity()
export class User {
  @PrimaryGeneratedColumn('uuid')
  id: string;

  @Column()
  @ApiProperty({
    example: '',
    description: 'username',
  })
  username: string;

  @ApiProperty({
    example: '',
    description: 'email',
  })
  @Column()
  email: string;

  @ApiProperty({
    example: '',
    description: 'password',
  })
  @Column()
  password: string;

  @CreateDateColumn()
  created_at: Date;

  @UpdateDateColumn()
  updated_at: Date;
}
