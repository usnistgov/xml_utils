""" Setup xml utils
"""

from os import chdir, pardir
from os.path import join, exists, dirname, normpath, abspath

from setuptools import find_packages, setup

reqs_default = join(dirname(__file__), "requirements.txt")
reqs_core = join(dirname(__file__), "requirements.core.txt")
required = []

if exists(reqs_default):
    with open(reqs_default) as f:
        required += f.read().splitlines()

if exists(reqs_core):
    with open(reqs_core) as f:
        required += f.read().splitlines()

with open(join(dirname(__file__), "README.rst")) as f:
    long_desc = f.read()

# Allow setup.py to be run from any path
chdir(normpath(join(abspath(__file__), pardir)))

setup(
    name="xml_utils",
    version="1.20.0",
    description="XML utils for the curator core project",
    long_description=long_desc,
    author="NIST IT Lab",
    author_email="itl_inquiries@nist.gov",
    url="https://github.com/usnistgov/xml_utils",
    packages=find_packages(),
    include_package_data=True,
    install_requires=required,
    extras_require={"Xerces": ["pyzmq==18.1.0", "xerces_wrapper==0.1.0"]},
)
