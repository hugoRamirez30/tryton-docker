FROM tryton/tryton:7.0

RUN pip install --break-system-packages trytond_party==7.0.* trytond_product==7.0.* trytond_stock==7.0.*

