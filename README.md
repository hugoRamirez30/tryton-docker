# ERP Basilios - Tryton

## Descripción

Este proyecto contiene la configuración completa del ERP Tryton para la empresa simulada Basilios. Incluye:

- Contenedores Docker para Tryton y PostgreSQL
- Archivo `basilios.sql` con la base de datos lista para usar
- Módulos de ventas, contabilidad, inventario y logística ya configurados

## Requisitos

- Docker y Docker Compose instalados
- Clonar este repositorio:

```bash
git clone https://github.com/hugoRamirez30/tryton-docker
cd erp-basilios

-levantar sistema

```bash
docker-compose up -d

-restaurar base de datos 
```bash
docker cp basilios.sql tryton-postgres:/basilios.sql
docker exec -it tryton-postgres bash
psql -U postgres -d tryton < /basilios.sql
exit

-acceder a tryton
```bash
http://localhost:8000


-exportar la base de datos 
```bash
docker exec -t tryton-postgres pg_dump -U postgres -d tryton > basilios.sql

