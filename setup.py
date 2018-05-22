from setuptools import setup

setup(name='Desire2Download',
	  version='1.0.0',
	  install_requires=[
	  		'BeautifulSoup',
	  		'mechanize',
	  ],
	  packages=['src'],
	  entry_points={
	  		'console_scripts': [
	  			'src = src.__main__:main'
	  		]
	  },
	  )