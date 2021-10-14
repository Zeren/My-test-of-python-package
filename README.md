# Otestovani nahravani na PYPI
Otestoval jsem si buildnuti package, nahravani modulu v ramci jednoho package (delal jsem to spatne), najrani na test pypi, nastaveni dependencies a jejich stahnuti pipem. 

Buildnuti package
```powershell
python -m pip install --upgrade build
python -m build
```

Nahrani na testovaci pypi
```powershell
python -m pip install --upgrade twine
python -m twine upload --repository testpypi --skip-existing dist/*
```

Stazeni z testovaciho pypi a stazeni dependencies z normalniho pypi
```powershell
python -m pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ Ukazka-pyside2==1.0.6
```
A pak normalni spusteni:
```powershell
python -m main
```
