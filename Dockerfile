FROM python:3.12-slim

# Instalamos las dependencias necesarias para Odoo
RUN apt-get update && apt-get install -y \
    build-essential \
    libxml2-dev \
    libssl-dev \
    libmariadb-dev \
    libpq-dev \
    libsasl2-dev \
    libldap2-dev \
    libjpeg62-turbo-dev \
    liblcms2-dev \
    libblas-dev \
    libatlas-base-dev \
    libopenblas-dev \
    libcurl4-openssl-dev \
    libfreetype6-dev \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /mnt

# Copiamos el código fuente de Odoo desde el directorio 'odoo'
COPY ./odoo /mnt/odoo

# Copiamos el archivo de configuración de Odoo
COPY ./odoo.conf /mnt/odoo.conf

# Copiamos el archivo requirements.txt para las dependencias de Python
COPY ./requirements.txt /mnt/requirements.txt

# Copiamos los addons estándar y los personalizados al contenedor
COPY ./minimal_addons /mnt/minimal_addons
COPY ./custom-addons /mnt/extra-addons

COPY ./setup /mnt/setup
COPY ./COPYRIGHT /mnt/COPYRIGHT
COPY ./LICENSE /mnt/LICENSE
COPY ./MANIFEST.in /mnt/MANIFEST.in
COPY ./odoo-bin /mnt/odoo-bin
COPY ./README.md /mnt/README.md
COPY ./SECURITY.md /mnt/SECURITY.md
COPY ./setup.cfg /mnt/setup.cfg
COPY ./setup.py /mnt/setup.py

# Instalamos las dependencias de Python

RUN pip install -r /mnt/requirements.txt

# Exponemos el puerto 8069 para Odoo
EXPOSE 8069

# Comando para ejecutar Odoo
CMD ["python", "/mnt/odoo-bin", "-c", "/mnt/odoo.conf", "-r", "odooAdmin", "-w", "odooPassDev", "--addons-path=minimal_addons,custom-addons"]