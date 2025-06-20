# tryton-docker

Este repositorio contiene el entorno de desarrollo para Tryton 7.0 utilizando Docker, PostgreSQL y módulos personalizados.

## 📦 Contenido

- `docker-compose.yml`: configuración base para levantar los contenedores.
- `trytond.conf`: archivo de configuración del servidor Tryton.
- `modules/`: carpeta que contiene los módulos personalizados.
- `files/`: archivos varios necesarios para la configuración.
- `tryton-client-web/`: cliente web de Tryton.
- `Estado_Instalacion_Tryton.txt`: resumen de la instalación y estado actual del entorno.
- `Dockerfile`: archivo para construir la imagen Docker.
- `README.md`: este archivo.

## ⚙️ Módulos personalizados

- `inventario_basilios`
- `proveedores_basilios`

Ambos se encuentran dentro de la carpeta `modules/` y están registrados correctamente en la base de datos, pero **no se muestran en el cliente Tryton**.

## 🚨 Problemas actuales

- Tryton no detecta los módulos personalizados a pesar de estar activos.
- Se han hecho pruebas de permisos, rutas y estructura de carpetas sin éxito.
- Las salidas y logs que se muestran en la terminal durante la instalación y ejecución no se reflejan en la interfaz web del cliente Tryton.
- Para mayor detalle sobre la instalación y estado, revisar `Estado_Instalacion_Tryton.txt`.

## 🧪 Pruebas realizadas

- Reconstrucción de imágenes y levantamiento de contenedores con `docker-compose up --build`.
- Revisión de rutas y permisos con comandos como `tree` y `ls -la`.
- Consultas SQL para verificar el estado y registro de los módulos en la base de datos.
- Inspección directa del servidor Tryton desde la terminal para detectar errores y estado.
- Verificación de la instalación de dependencias en el Dockerfile mediante pip.

## 📄 Contacto

Este entorno fue preparado por [Hugo Ramírez](https://github.com/hugoRamirez30) como parte de pruebas y personalización para Apimes.

---



