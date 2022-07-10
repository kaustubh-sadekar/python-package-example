# python-package-example
A simple example of how to create your own python package.

A detailed tutorial can be found [here](https://betterscientificsoftware.github.io/python-for-hpc/tutorials/python-pypi-packaging/).

## Folder structure

The folder structure for the project is as follows:

```text

 python_package_example
    ├── mathfun
    │   ├── arrays
    │   │   ├── basic.py
    │   │   ├── __init__.py
    │   │   └── others.py
    │   ├── __init__.py
    │   ├── ops
    │   │   ├── basic.py
    │   │   ├── __init__.py
    │   │   ├── others.py
    │   │   ├── powers.py
    │   │   └── __pycache__
    │   │       ├── basic.cpython-37.pyc
    │   │       ├── __init__.cpython-37.pyc
    │   │       ├── others.cpython-37.pyc
    │   │       └── powers.cpython-37.pyc
    │   ├── __pycache__
    │   │   └── __init__.cpython-37.pyc
    │   └── version.py
    └── setup.py
 ```
 
The article shared above also contains instructions to upload your package to PyPI. This repository is simply an easy to use example inspired by the article.
 
## Setup
 
Follow these instructions to install and test the mathfun package.
```script
pip install setuptools
pip install .
```

Make sure you are in the directory containing the setup.py when you run the above commands.

Refer [example1.py](example1.py) to understand how to your installed package.
 
