import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='sheetsDb',
    version='0.11',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',  # example license
    description="Use Google Sheets as Database",
    long_description=README,
    url="https://github.com/aswinzz/sheetsDb",
    author='aswinzz',
    author_email='iit2016106@iiita.ac.in',
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
)