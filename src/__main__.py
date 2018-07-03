import sys
import getopt
import re
import os
from desire2download import Desire2Download
from sys import platform

def usage():
	print('usage: Desire2Download [-u user] [-p  password] ... [-i ignoreRegex] [-c courseRegex] [-o overwrite]')
	sys.exit(2)

def main():

	try:
		opts, args = getopt.getopt(sys.argv[1:], 'hou:p:i:c:', ['help', 'overwrite', 'user=', 'pass=', 'ignore=', 'course='])
	except getopt.GetoptError:
		usage()

	username = None
	password = None
	path = None
	overwrite = False
	ignoreFiles = []
	ignoreCourses = []

	# First determine the platform the application is running in and set the phantomJS accordingly.
	if platform == "win32":
		# Windows
		path = os.path.abspath("../platform/windows/PhantomJS/bin/phantomjs.exe")
	elif platform == "darwin":
		# OS X
		path = os.path.abspath("../platform/mac/PhantomJS/bin/phantomjs")
		

	for opt, arg in opts:
		if opt in ('-h', '--help'):
			usage()
		if opt in ('-u', '--user'):
			username = arg
		if opt in ('-p', '--password'):
			password = arg
		if opt in ('-o', '--overwrite'):
			overwrite = True
		if opt in ('-i', '--ignore'):
			try:
				regex = re.compile(arg)
				ignoreFiles.append(regex)
			except:
				print('regex %s is invalid' % arg)
				sys.exit(2)
		if opt in ('-c', '--course'):
			try:
				regex = re.compile(arg)
				ignoreCourses.append(regex)
			except:
				print('regex %s is invalid' % arg)
				sys.exit(2)

	# Since user, pass and path are required fields, if one of them are None, return error message
	if username == None or password == None or path == None :
		usage()

	desire2Download = Desire2Download(username, password, overwrite, ignoreFiles, ignoreCourses, path)

	desire2Download.login()
	desire2Download.getContent()
	desire2Download.getCourseHome()
	desire2Download.tearDown()

if __name__ == '__main__' :
	main()
