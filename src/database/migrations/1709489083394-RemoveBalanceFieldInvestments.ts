import { MigrationInterface, QueryRunner } from "typeorm";

export class RemoveBalanceFieldInvestments1709489083394 implements MigrationInterface {
    name = 'RemoveBalanceFieldInvestments1709489083394'

    public async up(queryRunner: QueryRunner): Promise<void> {
        await queryRunner.query(`ALTER TABLE "investment" DROP COLUMN "balance"`);
    }

    public async down(queryRunner: QueryRunner): Promise<void> {
        await queryRunner.query(`ALTER TABLE "investment" ADD "balance" numeric(10,2) NOT NULL DEFAULT '0'`);
    }

}
