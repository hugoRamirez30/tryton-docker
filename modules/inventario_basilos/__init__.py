from trytond.pool import Pool
from . import model

def register():
    Pool.register(
        model.InventoryLine,
        model.DailyReconciliation,
        module='inventario_basilos',
        type_='model',
    )
