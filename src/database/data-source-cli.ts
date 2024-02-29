import 'dotenv/config';
import { DataSource, DataSourceOptions } from 'typeorm';

const dataSourceOptions: DataSourceOptions = {
  type: 'postgres',
  host: process.env.DATABASE_HOST,
  port: +process.env.DATABASE_PORT,
  username: process.env.DATABASE_USER,
  password: process.env.DATABASE_PASS,
  database: process.env.DATABASE_NAME,
  entities: [__dirname + '/../**/**.entity{.ts,.js}'],
  migrations: [__dirname + '/migrations/*.{js,ts}'],
};

const dataSource = new DataSource(dataSourceOptions);

export default dataSource;
