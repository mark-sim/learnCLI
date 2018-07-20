import sys
import getopt
import re
import os
from learnCLI import LearnCLI
from sys import platform

def usage():
	print('usage: Desire2Download [-u user] [-p  password]')
	sys.exit(2)

def main():

	try:
		opts, args = getopt.getopt(sys.argv[1:], 'hu:p:', ['help','user=', 'pass='])
	except getopt.GetoptError:
		usage()

	username = None
	password = None
	path = None

	# First determine the platform the application is running in and set the phantomJS accordingly.
	if platform == "win32":
		# Windows
		path = os.path.abspath("../platform/windows/Chrome/bin/chromedriver.exe")
	elif platform == "darwin":
		# OS X
		path = os.path.abspath("../platform/mac/Chrome/bin/chromedriver")
		

	for opt, arg in opts:
		if opt in ('-h', '--help'):
			usage()
		if opt in ('-u', '--user'):
			username = arg
		if opt in ('-p', '--password'):
			password = arg

	# Since user, pass and path are required fields, if one of them are None, return error message
	if username == None or password == None or path == None :
		usage()

	learnCLI = LearnCLI(username, password, path)

	learnCLI.login()
	learnCLI.getContent()
	learnCLI.getCourseHome()
	learnCLI.getInput()
	learnCLI.tearDown()

if __name__ == '__main__' :
	main()
