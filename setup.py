from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="QRdecomposition_pkg",
    version="0.0.1",
    author="Aya Aihara",
    author_email="aya.aihara@angstrom.uu.se",
    description="QR decomposition of a matrix using the orthogonal Householder transformation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aya02/projct",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['aide_design'],
)
