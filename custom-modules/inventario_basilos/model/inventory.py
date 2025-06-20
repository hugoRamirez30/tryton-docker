from trytond.model import Model, fields, ModelView
from trytond.pool import PoolMeta, Pool

# Extensión de Líneas de Inventario para Mermas
class InventoryLine(metaclass=PoolMeta):
    __name__ = 'stock.inventory.line'

    tipo_merma = fields.Selection([
        (None, ''),
        ('vencido', 'Vencido'),
        ('danado', 'Dañado'),
        ('otro', 'Otro'),
    ], 'Tipo de Merma')
    
    cantidad_merma = fields.Float("Cantidad Mermada")

# Modelo para Conciliación Diaria
class DailyReconciliation(ModelView, Model):
    __name__ = 'inventario_basilos.daily_reconciliation'
    
    fecha = fields.Date("Fecha", required=True)
    producto = fields.Many2One(
        'product.product', 
        "Producto", 
        required=True,
        domain=[('salable', '=', True)]  # Solo productos vendibles
    )
    ubicacion = fields.Many2One(
        'stock.location', 
        "Ubicación", 
        required=True
    )
    conteo_fisico = fields.Float("Conteo Físico", required=True)
    conteo_sistema = fields.Float("Conteo Sistema", readonly=True)
    diferencia = fields.Float(
        "Diferencia", 
        readonly=True,
        help="Diferencia = Conteo Físico - Conteo Sistema"
    )
    
    @classmethod
    def __setup__(cls):
        # Configuración inicial del modelo
        super(DailyReconciliation, cls).__setup__()
        
        # Agregar botón de actualización
        cls._buttons.update({
            'update_stock': {}
        })
    
    @classmethod
    def update_stock(cls, records):
        """
        Actualiza el conteo del sistema para los registros seleccionados
        """
        # Obtener el pool de productos
        Product = Pool().get('product.product')
        
        for record in records:
            if record.producto and record.ubicacion:
                # Obtener cantidad actual del sistema (Tryton 7.0)
                quantities = Product.get_quantity(
                    [record.producto.id], 
                    [record.ubicacion.id]
                )
                
                # Extraer el valor correcto de la estructura de datos
                if quantities and record.producto.id in quantities:
                    location_quantities = quantities[record.producto.id]
                    if record.ubicacion.id in location_quantities:
                        record.conteo_sistema = location_quantities[record.ubicacion.id]
                    else:
                        record.conteo_sistema = 0.0
                else:
                    record.conteo_sistema = 0.0
                
                # Calcular diferencia
                record.diferencia = record.conteo_fisico - record.conteo_sistema
                
                # Guardar los cambios
                cls.save([record])