# setup.py
from setuptools import setup, find_packages

setup(
    name="arca_arg",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "zeep",           # Cliente SOAP
        "cryptography",   # Firma digital
        "python-dateutil", # Manejo de fechas
        
    ],
    python_requires=">=3.8",
    author="Raul E. Lopez Briega",
    author_email="relopezbriega@gmail.com",
    description="API para interactuar con los Web Services de AFIP",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/relopezbriega/arca_arg",  # Reemplazar con tu repo
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
