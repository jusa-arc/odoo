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
python odoo-bin -r odooAdmin -w odooPassDev --addons-path=addons,custom-addons -d pegaso -i base

## iniciar con BD
python odoo-bin -r odooAdmin -w odooPassDev --addons-path=addons,custom-addons -d pegaso

## iniciar sin BD
python odoo-bin -r odooAdmin -w odooPassDev --addons-path=addons,custom-addons

## actualizar modulo
python odoo-bin -u point_of_sale -d pegaso -r odooAdmin -w odooPassDev --stop-after-init --dev=all --load=web

## crear custom module
python odoo-bin scaffold point_of_sale_custom custom-addons/

## levantar docker (automaticamente detecta el .env)
docker-compose up --build -d