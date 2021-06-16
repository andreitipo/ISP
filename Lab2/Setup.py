from setuptools import setup

setup(
    name='serializers',
    version='1.0',
    description='LR2',
    packages=['serializers'],
    author='Andrei Chaplinskiy',
    author_email='andreitipo@gmail.com',
    entry_points={ 'console_scripts': [ 'run = serializers.main:main'  ]})