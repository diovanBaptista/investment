import { MigrationInterface, QueryRunner } from "typeorm";

export class RelationUserAndInvestment1709304929763 implements MigrationInterface {
    name = 'RelationUserAndInvestment1709304929763'

    public async up(queryRunner: QueryRunner): Promise<void> {
        await queryRunner.query(`ALTER TABLE "investment" ADD "userId" uuid`);
        await queryRunner.query(`ALTER TABLE "investment" ADD CONSTRAINT "FK_e37ec642d341163666411eae841" FOREIGN KEY ("userId") REFERENCES "user"("id") ON DELETE NO ACTION ON UPDATE NO ACTION`);
    }

    public async down(queryRunner: QueryRunner): Promise<void> {
        await queryRunner.query(`ALTER TABLE "investment" DROP CONSTRAINT "FK_e37ec642d341163666411eae841"`);
        await queryRunner.query(`ALTER TABLE "investment" DROP COLUMN "userId"`);
    }

}
