# modules/basilios_proveedores/proveedores.py

from trytond.model import ModelSQL, ModelView, fields
from trytond.pool import PoolMeta

__metaclass__ = PoolMeta

class Party(ModelSQL, ModelView):
    'Extiende party.party para datos de Proveedores Basilios'
    __name__ = 'party.party'

    es_proveedor_fijo = fields.Boolean('Proveedor Fijo')
    categoria_proveedor = fields.Selection([
        ('bebidas', 'Bebidas'),
        ('harinas', 'Harinas e Insumos'),
        ('materiales', 'Materiales y Envases'),
        ('otros', 'Otros'),
    ], 'Categoría Proveedor')
    
    productos_suministrados = fields.One2Many(
        'party-party.product-template',  # coincide con el __name__ de PartyProductTemplate
        'party',
        'Productos Suministrados',
        help="Productos que este proveedor suministra regularmente"
    )

class PartyProductTemplate(ModelSQL, ModelView):
    "Tabla intermedia Proveedor ⇄ Producto"
    __name__ = 'party-party.product-template'

    party = fields.Many2One(
        'party.party', 'Proveedor', required=True, ondelete='CASCADE'
    )
    product = fields.Many2One(
        'product.template', 'Producto', required=True, ondelete='CASCADE'
    )
