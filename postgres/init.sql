-- Criação do usuário se não existir
DO $$
BEGIN
  IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'coderockr_admin') THEN
    CREATE USER coderockr_admin WITH PASSWORD 'coderockr';
  END IF;
END $$;

-- Criação do banco de dados se não existir
DO $$
BEGIN
  IF NOT EXISTS (SELECT FROM pg_database WHERE datname = 'coderockr') THEN
    CREATE DATABASE coderockr;
  END IF;
END $$;

-- Concessão de privilégios ao usuário no banco de dados
GRANT ALL PRIVILEGES ON DATABASE coderockr TO coderockr_admin;