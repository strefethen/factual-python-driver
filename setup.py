from setuptools import setup, find_packages

required = ['requests-oauth >= 0.3.0']

setup(
    name='factual-api',
    version='0.1',
    description='Official Python driver for the Factual public API',
    url='http://github.com/Factual/factual-python-driver',
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),
    keywords=['factual'],
    packages=find_packages(),
    install_requires=required
)
