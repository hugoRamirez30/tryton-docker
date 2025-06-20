# modules/inventario_basilos/setup.py
from setuptools import setup, find_packages

setup(
    name='inventario_basilos',
    version='1.0.0',
    description='Gestión de inventario y mermas',
    author='Hugo-Ramirez',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={
        'trytond.modules': [
            'inventario_basilos = inventario_basilos'
        ]
    },
)
