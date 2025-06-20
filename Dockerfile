FROM tryton/tryton:7.0

# Instala módulos base (asegúrate que estén instalados)
RUN pip install --break-system-packages trytond_stock trytond_product trytond_party

# Copia tus módulos personalizados en una carpeta distinta
COPY modules/ /usr/local/lib/python3.11/dist-packages/custom_modules/
