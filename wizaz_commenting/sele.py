
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import random
from db import db
import sys


# class selenium(db):
class selenium(db):

	def __init__(self,name):
		super().__init__(name)
		username=input("Enter your username: ")
		password=input('Enter your password: ')
		self.driver = webdriver.Chrome('C:/Users/Tomasz/Desktop/chromedriver_win32/chromedriver.exe')
		print("Logging...")
		self.driver.get("http://wizaz.pl/logowanie/")
		#login testow, password testow123
		self.driver.find_element_by_id('login_username').send_keys(str(password))
		self.driver.find_element_by_id('login_password').send_keys(str(password))
		time.sleep(3)
		self.driver.find_element_by_id('login_submit').click()
		# self.db=db
		self.random=0
		self.newrandom=0
		self.adv=['trwałość','kolor','cena','opakowanie','krycie','odcień']
		self.disadv=['trwałość','kolor','cena','opakowanie','krycie','odcień','pozostawia ślady','wydajność','wysusza skóre']


	def wizaz(self):
		driver=self.driver
		print("Going to product...")
		for i in range(1,11):
			driver.get("http://wizaz.pl/kosmetyki/makijaz/podklady?page={}".format(i))
			time.sleep(2)
			find=driver.find_elements_by_xpath("//*[@class='list-product']//h2//a")
			print("Products on this page: {}".format(len(find)))
			for j in range (0,len(find)):
				self.random_norepeat(1,10)
				# CHECK IF EXIST IN DATABASE
				time.sleep(1)
				find=driver.find_elements_by_xpath("//*[@class='list-product']//h2//a")
				if (self.check(find[j].get_attribute("href"))!=False):
					print("{} from {} to next page...".format((len(find)-j),len(find)))
					self.add(self.random,find[j].get_attribute("href"))
					driver.execute_script("arguments[0].click();", find[j])
					time.sleep(2)
					button=driver.find_element_by_class_name('add')
					driver.execute_script("arguments[0].click();", button)
					time.sleep(2)
					try:
						button.click()
						driver.execute_script("arguments[0].click();", button)
					except:
						print('juz jest')
					self.commenting(self.random,i)
				else:
					print("Already commented")
					continue


	def commenting(self,random_comment,i):
		driver=self.driver
		self.comments(random_comment)
		time.sleep(2)
		driver.find_element_by_id('review_add_title').send_keys(str(self.title))
		time.sleep(1)
		driver.find_element_by_id('review_add_contents').send_keys(str(self.comment))
		time.sleep(2)

		# adv
		sample=random.sample([0, 1, 2, 3, 4, 5],  random.randrange(2,6))
		adv=[]
		for k in sample:
			adv.append(self.adv[k])
		adv_str=', '.join(str(e) for e in adv)
		print("ADV:",adv_str)
		driver.find_element_by_id('review_add_advantages').send_keys(str(adv_str))
		time.sleep(2)
		
		# dis
		sample=random.sample([0, 1, 2, 3, 4, 5, 6, 7, 8],  random.randrange(1,4))
		disadv=[]
		for k in sample:
			if self.disadv[k] not in adv:
				disadv.append(self.disadv[k])
			else:
				continue
		disadv_str=', '.join(str(e) for e in disadv)
		print('DISADV:',disadv_str)
		driver.find_element_by_id('review_add_disadvantages').send_keys(str(disadv_str))
		time.sleep(2)

		select=driver.find_element_by_id('review_add_rate_%d' % (random.randrange(2,5)))
		driver.execute_script("arguments[0].click();", select)
		try:
			select=driver.find_element_by_id('review_add_rate_additional_1_%d' % (random.randrange(2,5)))
			driver.execute_script("arguments[0].click();", select)
			select=driver.find_element_by_id('review_add_rate_additional_2_%d' % (random.randrange(2,5)))
			driver.execute_script("arguments[0].click();", select)
			select=driver.find_element_by_id('review_add_rate_additional_3_%d' % (random.randrange(2,5)))
			driver.execute_script("arguments[0].click();", select)
			select=driver.find_element_by_id('review_add_rate_additional_4_%d' % (random.randrange(2,5)))
			driver.execute_script("arguments[0].click();", select)
			select=driver.find_element_by_id('review_add_rate_additional_5_%d' % (random.randrange(2,5)))
			driver.execute_script("arguments[0].click();", select)
		except:
			print ("Unexpected error: {}".format(sys.exc_info()[0]))
		select=driver.find_element_by_id('review_add_buy_again_{}'.format(random.randrange(266,269)))
		driver.execute_script("arguments[0].click();", select)
		time.sleep(1)
		select=Select(driver.find_element_by_id('review_add_used_for_type'))
		select.select_by_value("{}".format(random.randrange(2,6)))
		select=Select(driver.find_element_by_id('review_add_used_packaging_amount'))
		select.select_by_value('{}'.format(random.randrange(275,280)))
		time.sleep(1)
		select=driver.find_element_by_id('review_add_review_where_purchased_14')
		driver.execute_script("arguments[0].click();", select)
		time.sleep(1)
		select=driver.find_element_by_id('review_add_submit')
		driver.execute_script("arguments[0].click();", select)
		time.sleep(4)
		print("Comment Added!")
		driver.get("http://wizaz.pl/kosmetyki/makijaz/podklady?page={}".format(i))
		time.sleep(12)


	def random_norepeat(self,start,end):
		while self.random==self.newrandom:
			self.random=random.randrange(start,end)
		self.newrandom=self.random


if __name__ == "__main__":
	# db=db.db('database.db')
	sele=selenium('database.db')
	sele.wizaz()