from setuptools import setup

setup(
    name='nubergcli',
    version='0.1.0',
    packages=['nubergcli'],
    entry_points={
        'console_scripts': [
            'nubergcli = nubergcli.__main__:main'
        ]
    })
