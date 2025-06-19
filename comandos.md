docker-compose down -v
docker-compose up -d

## crear base de datos
python odoo-bin -r odooAdmin -w odooPassDev --addons-path=addons -d odooLibreria -i base

## iniciar con BD
python odoo-bin -r odooAdmin -w odooPassDev --addons-path=addons -d odooLibreria

## iniciar sin BD
python odoo-bin -r odooAdmin -w odooPassDev --addons-path=addons