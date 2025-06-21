from trytond.pool import Pool
from . import model


def register():
    Pool.register(
        model.Party,
        model.PartyProductTemplate,
        module='basilios_proveedores',
        type_='model'
    )
