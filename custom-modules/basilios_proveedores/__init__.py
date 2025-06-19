from trytond.pool import Pool
from . import proveedores

def register():
    Pool.register(
        proveedores.Party,
        proveedores.PartyProductTemplate,
        module='basilios_proveedores', type_='model'
    )
