from setuptools import setup

setup(name='LearnCLI',
	  version='1.0.0',
	  description='Command Line Interface of Learn',
	  author='Mark Sim',
	  install_requires=[
	  		'selenium',
	  		'dropbox',
	  ],
	  packages=['src'],
	  entry_points={
	  		'console_scripts': [
	  			'src = src.__main__:main'
	  		]
	  },
	)