from setuptools import setup, find_packages

required = ['requests-oauth >= 0.3.0']

setup(
    name='factual-api',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/Factual/factual-python-driver',
    description='Official Python driver for the Factual public API',
    install_requires=required
)
