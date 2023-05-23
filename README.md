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
pip install . # SUCCESS
pip install --no-use-pep-517 . # SUCCESS

## First failed build mode
pip install --use-pep517       # FAILURE

## Second failed build mode
touch pyproject.toml
python3 setup.py bdist_wheel
pip install .                  # FAILURE
pip install --use-pep517 .     # FAILURE
pip install --no-use-pep517 .  # SUCCESS

## Third failed build mode
mv pyproject.toml.new pyproject.toml   # Use a basic pyproject.toml with backend and project info
python3 setup.py bdist_wheel   # FAILURE
```
