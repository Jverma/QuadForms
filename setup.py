#!/usr/bin/env python

from setuptools import setup, find_packages
import os
import sys

sys.path.insert(0, 'QuadFormsDistribution')

sys.path.pop(0)

packages = ['QuadForms']

setup(
	name='quadforms',
	version='0.20',
	author='Janu Verma',
	author_email='jv367@cornell.edu',
	description='Distribution function of a linear combination of quadratic forms',
	url='https://github.com/Jverma/QuadForms',
	platforms=['Linux','Mac OSX', 'Windows', 'Unix'],
	classifiers=[
	'Development Status :: 3 - Alpha',
	'Intended Audience :: Developers',
	'License :: MIT License',
	'Operating System :: OS Independent',
	'Progamming Language :: Python',
	'Topic :: Software Development :: Libraries :: Python Modules'],
	packages=packages,
	package_data={'QuadForms':['Data/*.txt']},
	license='MIT'
	)			
	