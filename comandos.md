## configurar docker

  ## db/init.sql
  CREATE DATABASE odooLibreria;
  CREATE ROLE odooAdmin WITH LOGIN PASSWORD 'password';
  ALTER ROLE odooAdmin CREATEDB;
  GRANT ALL PRIVILEGES ON DATABASE odooLibreria TO odooAdmin;

  ## .env
  POSTGRES_USER=odooAdmin
  POSTGRES_PASSWORD=password
  POSTGRES_DB=odooLibreria


## comandos docker
docker-compose down -v
docker-compose up -d

## crear base de datos
python odoo-bin -r odooAdmin -w odooPassDev --addons-path=addons -d odooLibreria -i base

## iniciar con BD
python odoo-bin -r odooAdmin -w odooPassDev --addons-path=addons -d odooLibreria

## iniciar sin BD
python odoo-bin -r odooAdmin -w odooPassDev --addons-path=addons