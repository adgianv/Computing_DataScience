from setuptools import find_packages, setup

setup(
    name='diabetes_mellitus_library',
    packages=find_packages(),
    version='0.1.0',
    description='Python Library for hmw4',
    author='Viktoriia Yuzkiv, Angelo Di Gianvito, Oliver Gatland',
    install_requires=['pandas', 'numpy', 'scikit-learn']
)