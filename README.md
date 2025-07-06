# ERP Basilios - Tryton

## Descripción
Este proyecto contiene la configuración y base de datos para el sistema ERP Tryton de la empresa simulada Basilios. Incluye:

- Contenedores Docker para Tryton y PostgreSQL
- Archivo `basilios.sql` con la base de datos completa
- Configuración para facturación, inventarios, contabilidad y ventas
- Archivos `docker-compose.yml` y `trytond.conf` para levantar el sistema

---

## Requisitos

- Tener instalado Docker y Docker Compose
- Clonar este repositorio

---

## Levantar el sistema

Desde la carpeta raíz del proyecto (`tryton-docker`), ejecutar:

```bash
docker-compose up -d

Restaurar la base de datos
Para cargar la base de datos basilios.sql en el contenedor PostgreSQL:

Copiar el archivo al contenedor:

```bash
docker cp basilios.sql tryton-postgres:/basilios.sql

Entrar al contenedor PostgreSQL:

```bash
docker exec -it tryton-postgres bash

Restaurar la base:

```bash
psql -U postgres -d tryton < /basilios.sql

Salir del contenedor:

Acceder a Tryton
Después de levantar el sistema, Tryton estará disponible en:

http://localhost:8000

Exportar base de datos
Para hacer una copia de seguridad de la base de datos desde el contenedor PostgreSQL:

```bash
docker exec -t tryton-postgres pg_dump -U postgres -d tryton > basilios.sql