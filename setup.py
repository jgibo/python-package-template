from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = ""

setup(
    name="package_name",
    version=VERSION,
    author="",
    author_email="",
    description=DESCRIPTION,
    long_description=open('README.md').read(),
    url="<github repository url>",
    packages=find_packages(),
    install_requires=[]
)