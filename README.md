# tryton-docker

Este repositorio contiene el entorno de desarrollo para Tryton 7.0 utilizando Docker, PostgreSQL y módulos personalizados.

## 📦 Contenido

- `docker-compose.yml`: configuración base para levantar los contenedores.
- `trytond.conf`: archivo de configuración del servidor Tryton.
- `custom-modules/`: carpeta que contiene los módulos personalizados.
- `log/`: errores críticos recopilados.
- `terminal-output/`: salida de terminal útil para depuración.
- `notas/`: notas técnicas sobre configuración, pruebas y hallazgos.

## ⚙️ Módulos personalizados

- `inventario_basilios`
- `proveedores_basilios`

Ambos se encuentran en `/custom-modules` y están registrados correctamente en la base de datos, pero **no se muestran en el cliente Tryton**.

## 🚨 Problemas actuales

- Tryton no detecta los módulos personalizados a pesar de estar activos.
- Se han hecho pruebas de permisos, rutas, y estructura de carpetas sin éxito.
- Ver logs en `log/` y `terminal-output/`.

## 🧪 Pruebas realizadas

- Docker rebuild (`docker-compose up --build`)
- Revisar rutas con `tree` y `ls -la`
- Consultas SQL para verificar estado en la BD
- Inspección del servidor desde terminal

## 📄 Contacto

Este entorno fue preparado por [Hugo Ramírez](https://github.com/hugoRamirez30) como parte de pruebas y personalización para Apimes.

---


