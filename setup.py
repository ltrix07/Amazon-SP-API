from setuptools import setup, find_packages
from amazon_sp_api import __version__

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='amazon_sp_api',
    version=__version__,
    packages=find_packages(),
    install_requires=requirements,
    description='Library for Amazon SP API',
    author='ltrix07',
    author_email='ltrix02@gmail.com',
    url='https://github.com/ltrix07/amazon-sp-api'
)
