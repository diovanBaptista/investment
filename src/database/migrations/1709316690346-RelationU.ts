import { MigrationInterface, QueryRunner } from "typeorm";

export class RelationU1709316690346 implements MigrationInterface {
    name = 'RelationU1709316690346'

    public async up(queryRunner: QueryRunner): Promise<void> {
        await queryRunner.query(`ALTER TABLE "investment" DROP COLUMN "username"`);
    }

    public async down(queryRunner: QueryRunner): Promise<void> {
        await queryRunner.query(`ALTER TABLE "investment" ADD "username" character varying NOT NULL`);
    }

}
