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
python odoo-bin -r odooAdmin -w odooPassDev --addons-path=addons -d pegaso -i base

## iniciar con BD
python odoo-bin -r odooAdmin -w odooPassDev --addons-path=addons -d pegaso

## iniciar sin BD
python odoo-bin -r odooAdmin -w odooPassDev --addons-path=addons

## actualizar modulo
python odoo-bin -u point_of_sale -d pegaso -r odooAdmin -w odooPassDev --stop-after-init --dev=all --load=web