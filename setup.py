from distutils.core import setup
from os import path
import os

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))

description = 'An example python package'

long_description = description

version = '0.1.0'

setup(
  name = 'mathfun', # Name of the package
  packages = ['mathfun'], # name of the folder containing the package (ideally keep it same as the package name)
  version = version,
  license='MIT',        
  description = description,
  long_description=long_description,
  long_description_content_type="text/x-rst",
  author = 'Kaustubh Sadekar',
  keywords = ['Computer Vision', 'Helper functions'],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',   
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
