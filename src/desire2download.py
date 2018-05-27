import mechanicalsoup as ms
from selenium import webdriver
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

			# Check if it login credentials is correct
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

		# Sleep for 5 seconds to let javascript load. 5 seconds should be enough for most computers.
		time.sleep(5)

		courseElements = self.browser.find_elements_by_xpath(courses)

		courseInfoDict = {}

		for course in courseElements:
			# print('Adding ' + course.text + ' and ' + course.get_attribute("href"))
			courseInfoDict[course.text] = course.get_attribute("href")

		self.courseInfoDict = courseInfoDict

	def getCourseHome(self) :
		self.removeIgnoreCourses()

		# for each course, open the URI.
		for courseName in self.courseInfoDict :
			self.browser.get(self.courseInfoDict[courseName])
			print(courseName + self.courseInfoDict[courseName])

	
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
		