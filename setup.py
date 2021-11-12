from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='EDSC',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/alhaji779/mypackage',
    author='Michael Kanu',
    author_email='michaelkanu01@yahoo.com'
)