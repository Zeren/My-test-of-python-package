from setuptools import setup, find_packages

setup(
    name='Ukazka_pyside2',
    version='1.0.6',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    url='https://github.com/Zeren/python_test_pyside2',
    license='Creative Commons Zero v1.0 Universal',
    author='Jan Spacil',
    author_email='zeren.yuufana@gmail.com',
    description='Testing of how to do things correctly',
    install_requires=['pyside2', 'numpy']
)
