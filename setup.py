from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in perpustakaan/__init__.py
from perpustakaan import __version__ as version

setup(
	name="perpustakaan",
	version=version,
	description="1",
	author="2",
	author_email="3",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
