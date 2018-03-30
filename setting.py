# -*- coding:utf-8 -*-
import random

class Setting():
	#存储《guess-a-number》中的设置的类
	
	def __init__(self):
		#将判断条件初始设置为True
		self.begin =True
		self.switch = True
		self.num = random.randint(1,101)
