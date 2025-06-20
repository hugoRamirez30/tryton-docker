FROM tryton/tryton:7.0

RUN pip install trytond_stock trytond_product trytond_party

COPY custom-modules/inventario_basilos /usr/local/lib/python3.11/dist-packages/trytond/modules/inventario_basilos
COPY custom-modules/basilios_proveedores /usr/local/lib/python3.11/dist-packages/trytond/modules/basilios_proveedores

COPY trytond.conf /etc/trytond.conf
