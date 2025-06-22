from setuptools import setup, find_packages

setup(
    name='inventario_basilos',
    version='1.0.0',
    description='Gestión de inventario y mermas',
    author='Hugo-Ramirez',
    packages=find_packages(),  # detecta automáticamente las carpetas con código
    include_package_data=True,
    package_data={
        'inventario_basilos': ['tryton.cfg', 'ir.model.access.csv', 'view/*.xml'],
    },
    zip_safe=False,
    entry_points={
        'trytond.modules': [
            'inventario_basilos = inventario_basilos'
        ]
    },
)
