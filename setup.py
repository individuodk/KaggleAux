from setuptools import setup, find_packages
import os
import sys

with open('requirements.txt', 'r') as req:
    requirements = [i.replace('\n', '') for i in req]

setup(
    packages=find_packages(),
    install_requires=requirements
)
