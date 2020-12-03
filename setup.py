#!usr/bin/env python

from setuptools import setup, find_packages

setup(name="executable-boilerplate",
	version="0.1",
	description="Test for pip install git+",
	url="https://github.com/moaible/python-pip-executable-boilerplate",
	install_requires=['library-boilerplate @ git+https://git@github.com/moaible/python-pip-library-boilerplate.git'],
	packages=find_packages(),
	entry_points="""
	[console_scripts]
	boilerplate = executable.executable:main
	""",
	)
