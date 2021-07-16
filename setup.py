from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in volunteer/__init__.py
from volunteer import __version__ as version

setup(
	name='volunteer',
	version=version,
	description='Volunteer App',
	author='Hadia',
	author_email='ha-dia1995@hotmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
