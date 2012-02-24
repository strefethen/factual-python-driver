from setuptools import setup

required = ['requests-oauth >= 0.3.0']
packages = ['factual']

setup(
    name='factual-api',
    version='0.1',
    packages=packages,
    url='https://github.com/Factual/factual-python-driver',
    description='Official Python driver for the Factual public API',
    install_requires=required
)
