from setuptools import setup, find_packages

setup(
    name='inventario_basilos',
    version='1.0.0',
    description='Gestión de inventario y mermas',
    author='Hugo-Ramirez',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'inventario_basilos': ['tryton.cfg', 'ir.model.access.csv', 'view/*.xml'],
    },
    zip_safe=False,
    install_requires=[
        'trytond >=7.6,<7.7',
    ],
    entry_points={
        'trytond.modules': [
            'inventario_basilos = inventario_basilos'
        ]
    },
)
