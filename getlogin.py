#!/usr/bin/python

import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class getlogin:
    username = ''
    password = ''
    d = ''


    def __init__(self, username='System.User', password=''):
        self.username = username
        self.password = password

    def printClass(self):
        print ("getlogin stats: " + self.username + " " + self.password + " " + self.d.name)
    def openBrowser(self, whichBrowser="Firefox"):
#        self.printClass()
#        if self.d == '':
#            self.d = webdriver.Firefox()
        self.d = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                                  desired_capabilities=DesiredCapabilities.FIREFOX)

        

    def findLoginElement(self):
        print "Hi!"
    def doNothing(self):
	pass

#    def getpage(self, pageName="http://www.google.com", newTab=true): 
    def getpage(self, pageName="http://www.google.com"): 

#        self.d.send_keys(Keys.CONTROL + "t")
        self.d.get(pageName)
#        if newTab == true:
#            body = self.d.find_element_by_name("body")
#            url = Keys.CONTROL + "t" "http://www.google.com"
#            self.d.get(url)

    def closeBrowser(self):
        self.d.quit()
        self.d = ''
