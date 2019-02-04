from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import random
import sys

class selenium():
	def __init__(self):
		username=input("Enter your username: ")
		password=input('Enter your password: ')
		self.driver = webdriver.Chrome()
		print("Logging...")
		self.driver.get("http://wizaz.pl/logowanie/")
		#login testow2, password testow123
		self.driver.find_element_by_id('login_username').send_keys(str(password))
		self.driver.find_element_by_id('login_password').send_keys(str(password))
		time.sleep(2)
		self.driver.find_element_by_id('login_submit').click()
		self.random=0
		self.newrandom=0

	def wizaz_like(self):
		driver=self.driver
		print("Going to product...")
		for i in range(1,11):
			driver.get("https://wizaz.pl/kosmetyki/profil,2661833,testow.html")
			time.sleep(1)
			find=driver.find_elements_by_xpath("//div[@class='hit']//a[@rel='nofollow']")
			print('Products to liked: ',len(find))
			for j in range (0,len(find)):
				find=driver.find_elements_by_xpath("//div[@class='hit']//a[@rel='nofollow']")
				time.sleep(1)
				driver.execute_script("arguments[0].click();", find[j])
				time.sleep(3)
				is_active=driver.find_element_by_xpath("//*[@class='clearfix review glow']//*[@class='ng-scope']//*[@class='ng-isolate-scope']//a").get_attribute("class")
				if is_active!='upvote active':
				# nick=driver.find_elements_by_xpath("//*[@class='review glow']//header//div[@class='user-tag']//div[@class='h2']//a//span")
					like=driver.find_element_by_xpath("//*[@class='clearfix review glow']//*[@class='ng-scope']//*[@class='ng-isolate-scope']")
					driver.execute_script("arguments[0].click();", like)
					print("LIKE IT! Going back...")
					driver.get("https://wizaz.pl/kosmetyki/profil,2661833,testow.html")
				else:
					print('Already Liked! Going back...')
					driver.get("https://wizaz.pl/kosmetyki/profil,2661833,testow.html")

					


if __name__ == "__main__":
	sele=selenium()
	sele.wizaz_like()