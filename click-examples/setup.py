# To help use the python module as a command line tool
from setuptools import setup

setup(
    name="myhello",
    version='0.1',
    py_modules=['hello'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        myhello=hello:cli
    ''',
)