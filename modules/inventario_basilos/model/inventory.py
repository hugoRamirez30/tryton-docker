from trytond.model import ModelSQL, ModelView, fields
from trytond.pool import PoolMeta, Pool

__metaclass__ = PoolMeta

class InventoryLine(ModelSQL, ModelView):
    'Extiende stock.inventory.line para gestión de mermas'
    __name__ = 'stock.inventory.line'

    tipo_merma = fields.Selection([
        (None, ''),
        ('vencido', 'Vencido'),
        ('danado', 'Dañado'),
        ('otro', 'Otro'),
    ], 'Tipo de Merma')

    cantidad_merma = fields.Float('Cantidad Mermada')

class DailyReconciliation(ModelSQL, ModelView):
    'Conciliación Diaria de Inventario'
    __name__ = 'inventario_basilos.daily_reconciliation'

    fecha = fields.Date('Fecha', required=True)
    producto = fields.Many2One(
        'product.product', 'Producto', required=True,
        domain=[('salable', '=', True)]
    )
    ubicacion = fields.Many2One(
        'stock.location', 'Ubicación', required=True
    )
    conteo_fisico = fields.Float('Conteo Físico', required=True)
    conteo_sistema = fields.Float('Conteo Sistema', readonly=True)
    diferencia = fields.Float(
        'Diferencia', readonly=True,
        help='Diferencia = Conteo Físico - Conteo Sistema'
    )

    @classmethod
    def __setup__(cls):
        super(DailyReconciliation, cls).__setup__()
        cls._buttons.update({
            'update_stock': {}
        })

    @classmethod
    def update_stock(cls, records):
        'Actualiza el conteo del sistema usando stock.actual'
        Product = Pool().get('product.product')
        for rec in records:
            # Obtener cantidades
            quantities = Product.get_quantity(
                [rec.producto.id], [rec.ubicacion.id]
            ) or {}
            rec.conteo_sistema = (
                quantities.get(rec.producto.id, {})
                         .get(rec.ubicacion.id, 0.0)
            )
            rec.diferencia = rec.conteo_fisico - rec.conteo_sistema
        cls.save(records)