# modules/basilios_proveedores/setup.py
from setuptools import setup, find_packages

setup(
    name='basilios_proveedores',
    version='1.0.0',
    description='Gestión de proveedores fijos para Basilios Panadería',
    author='Hugo-Ramirez',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={
        'trytond.modules': [
            'basilios_proveedores = basilios_proveedores'
        ]
    },
)
