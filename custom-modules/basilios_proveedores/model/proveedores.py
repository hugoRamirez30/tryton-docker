from trytond.model import Model, fields
from trytond.pool import PoolMeta

class Party(metaclass=PoolMeta):
    __name__ = 'party.party'

    es_proveedor_fijo = fields.Boolean("Proveedor Fijo")
    categoria_proveedor = fields.Selection([
        ('bebidas', 'Bebidas'),
        ('harinas', 'Harinas e Insumos'),
        ('materiales', 'Materiales y Envases'),
        ('otros', 'Otros'),
    ], 'Categoría Proveedor')
    
    productos_suministrados = fields.Many2Many(
        'party-party.product-template', 
        'party', 
        'product', 
        'Productos Suministrados',
        help="Productos que este proveedor suministra regularmente"
    )

class PartyProductTemplate(Model):
    "Relación Proveedor-Producto"
    __name__ = 'party-party.product-template'
    party = fields.Many2One('party.party', 'Proveedor', required=True, ondelete='CASCADE')
    product = fields.Many2One('product.template', 'Producto', required=True, ondelete='CASCADE')
