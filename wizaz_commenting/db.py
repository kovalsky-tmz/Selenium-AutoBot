import sqlite3
import random

class db(object):
	def __init__(self,name):
		self.name=name
		self.conn = sqlite3.connect(self.name)
		if(self.conn): print ('Connected')	
		

	def comments(self,random):
		query=self.conn.execute("SELECT * FROM comments WHERE Id={}".format(random))
		for x in query:
			self.title=str(x[4])
			self.comment=str(x[1])
			# self.adv=str(x[2])
			# self.disadv=str(x[3])
			# print("ADV:{},DISADV:{}".format(self.adv, self.disadv))
			print("Commenting...")
			print("ACTUALY COMMENTED: \n Title: {} \n".format(self.title))
			print("Commenting...")
			
	def add(self,id,url):
		self.conn.execute('INSERT INTO base (Comm_id,title) VALUES (?,?)',(id,url))
		print('RECORD URL ADDED - {}'.format(url))
		self.conn.commit()

	def check(self,url):
		query=self.conn.execute("SELECT * FROM base")
		for x in query:
			self.base_title=x[2]
			self.comment_id=x[1]
			if self.base_title in url:
				return False

	





