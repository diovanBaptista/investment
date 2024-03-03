import { MigrationInterface, QueryRunner } from "typeorm";

export class UpdateInvestments1709476667662 implements MigrationInterface {
    name = 'UpdateInvestments1709476667662'

    public async up(queryRunner: QueryRunner): Promise<void> {
        await queryRunner.query(`ALTER TABLE "investment" ADD "withdraw" boolean NOT NULL DEFAULT false`);
        await queryRunner.query(`ALTER TABLE "investment" ADD "withdraw_at" TIMESTAMP`);
        await queryRunner.query(`ALTER TABLE "investment" ADD "balance" numeric(10,2) NOT NULL DEFAULT '0'`);
    }

    public async down(queryRunner: QueryRunner): Promise<void> {
        await queryRunner.query(`ALTER TABLE "investment" DROP COLUMN "balance"`);
        await queryRunner.query(`ALTER TABLE "investment" DROP COLUMN "withdraw_at"`);
        await queryRunner.query(`ALTER TABLE "investment" DROP COLUMN "withdraw"`);
    }

}
