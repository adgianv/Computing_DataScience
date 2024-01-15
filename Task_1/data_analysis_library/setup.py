from setuptools import setup, find_packages

setup(
    name="data_analysis",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "scikit-learn",
    ],
)
