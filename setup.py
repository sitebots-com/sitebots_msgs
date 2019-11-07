## ! DO NOT MANUALLY INVOKE THIS setup.py, USE CATKIN INSTEAD

from distutils.core import setup
from setuptools import setup, find_packages
from catkin_pkg.python_setup import generate_distutils_setup

print(find_packages(where="src"))
# fetch values from package.xml
setup_args = generate_distutils_setup(
        packages=find_packages(where="src"),
        package_dir={'': 'src'},
)

setup(**setup_args)
