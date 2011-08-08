# -*- coding: utf-8 -*-
from setuptools import setup

version = "0.0.1"
readme = open("README.rst").read()

setup(name="pycompiler",
      version=version,
      description="Simple way to build a compiler",
      long_description=readme,
      author="Ângelo Otávio Nuffer Nunes",
      author_email="angelonuffer@gmail.com",
      packages=["pycompiler"],
      )
