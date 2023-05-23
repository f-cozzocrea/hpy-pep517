# hpy-pep517
pep517 debugging repo

Hpy version 0.9.0rc2

OS: Ubuntu 22.04

Steps to reproduce:
```
### env setup
python3 -m venv venv/hpy-pep517/
source venv/hpy-pep517/bin/activate
pip install --upgrade pip
pip install --upgrade setuptools wheel
pip install --pre hpy

## Successful build
python3 setup.py bdist_wheel
pip install dist/*.whl # SUCCESS

## Failed build
mv pyproject.toml.new pyproject.toml   # Use a basic pyproject.toml with backend and project info
python3 setup.py bdist_wheel   # FAILURE
```
