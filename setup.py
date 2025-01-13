from setuptools import setup, find_packages

setup(
    name='ml_detectors', 
    version='1.0', 
    packages=find_packages(),
    install_requires=['datasets', 'scikit-learn']
    )