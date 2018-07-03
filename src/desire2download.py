import mechanicalsoup as ms
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup as bs
import time
import sys

class Desire2Download:

	def __init__(self, username, password, overwrite, ignoreFiles, ignoreCourses, path) :
		self.username = username
		self.password = password
		self.overwrite = overwrite
		self.ignoreFiles = ignoreFiles
		self.ignoreCourses = ignoreCourses
		self.path = path
		self.url = "https://learn.uwaterloo.ca"

	def login(self) :
		xpaths = { 'usernameTxtBox' : "//input[@name='username']",
				   'passwordTxtBox' : "//input[@name='password']",
				   'submitButton' : "//input[@name='submit']"
				 }
		try:
			browser = webdriver.PhantomJS(executable_path = self.path)
			# Set fake browser size before doing get. This is to avoid 'Element is not currently visible and may not be manipulated' exception
			browser.set_window_size(1124, 850)
			browser.get(self.url)

			# Output Message
			print("Logging in to " + self.url + "...")

			# Clear the username textbox if already allowed by "Remember me".
			browser.find_element_by_xpath(xpaths['usernameTxtBox']).clear()

			# Write username in Username textbox
			browser.find_element_by_xpath(xpaths['usernameTxtBox']).send_keys(self.username)

			# Clear password textbox if already allowed by "Remember me"
			browser.find_element_by_xpath(xpaths['passwordTxtBox']).clear()

			# Write password in Password textbox
			browser.find_element_by_xpath(xpaths['passwordTxtBox']).send_keys(self.password)

			# Click login button
			browser.find_element_by_xpath(xpaths['submitButton']).click()

			# Check if its login credentials is correct
			if browser.current_url != self.url + "/d2l/home" :
				print("Error: Invalid username or password")
				sys.exit(2)

			# Output Message
			print("Logged in.")

			self.browser = browser

		except KeyboardInterrupt:
			browser.close()

	def getContent(self) :
		# This is the element which lists all the courses 
		# (Can't use BeautifulSoup or MechanicalSoup due to new learn updates)
		courses = "//a[@class='d2l-image-tile-base-link style-scope d2l-image-tile-base']"

		# Increasing time will guarantee javascript loading but 5 sec should be enough in most cases.
		time.sleep(5)

		courseElements = self.browser.find_elements_by_xpath(courses)
		courseInfoDict = {}

		for course in courseElements:
			# print('Adding ' + course.text + ' and ' + course.get_attribute("href"))
			courseInfoDict[course.text] = course.get_attribute("href")

		self.courseInfoDict = courseInfoDict

	# This method is basically called when app logged into learn and lists all the courses and commands available.
	def getCourseHome(self) :
		self.removeIgnoreCourses()

		toPrint = self.getCommands()

		# print for init.
		toPrint += "\nList of all the courses:\n"

		# for each course, open the URI.
		for courseName in self.courseInfoDict :
			toPrint += "- " + courseName + "\n"

		print(toPrint)

	def getCommands(self) :
		toRet = "\nList of available commands:\n"

		toRet += "- ls: list information about files in current directory\n"
		toRet += "- cd: change directory\n"
		toRet += "- d2d: downloads specified file and drops it to your dropbox\n"
		toRet += "       If file is not specified then everything under the current directory\n"
		toRet += "       will be downloaded and dropped into your dropbox\n"

		return toRet

	def removeIgnoreCourses(self) :
		for ignoreCourseRegex in self.ignoreCourses :
			listOfKeysToRemove = []
			# Iterate through course names and add any courses that need to be ignored
			for courseNames in self.courseInfoDict :
				if (ignoreCourseRegex.search(courseNames)) :
					listOfKeysToRemove.append(courseNames)

			# Now actually delete those courses in the dictionar y
			for keyToBeRemoved in listOfKeysToRemove :
				del self.courseInfoDict[keyToBeRemoved]


	def tearDown(self) :
		self.browser.close()
		