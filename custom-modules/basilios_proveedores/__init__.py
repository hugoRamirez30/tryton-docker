from trytond.pool import Pool

from .model import Party, PartyProductTemplate

def register():
    Pool.register(
        Party,
        PartyProductTemplate,
        module='basilios_proveedores', type_='model'
    )
