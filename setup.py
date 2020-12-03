#!usr/bin/env python

from setuptools import setup, find_packages

setup(name="executable-boilerplate",
	version="0.1",
	description="Test for pip install git+",
	url="https://github.com/moaible/python-pip-executable-boilerplate",
	packages=find_packages(),
	entry_points="""
	[console_scripts]
	boilerplate = boilerplate.boilerplate:main
	""",
	)
