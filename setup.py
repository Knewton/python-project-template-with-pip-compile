#!/usr/bin/env python
from setuptools import find_packages, setup


setup(
    name="Python Dependency Management Project Template with pip-compile",
    version="0.1.dev0",
    url="https://github.com/Knewton/python-project-template-with-pip-compile",
    author="Paul Kernfeld",
    author_email="oss@knewton.com",
    license="License :: OSI Approved :: Apache Software License",
    packages=find_packages(),
    include_package_data=True,
    install_requires=open("requirements.in").readlines(),
    tests_require=open("requirements.testing.in").readlines(),
    description="An explanatory Python project template using pip-compile for dependency "
                "management",
    long_description="\n" + open("README.md").read(),
)
