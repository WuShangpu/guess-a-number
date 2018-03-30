# -*- coding:utf-8 -*-
class Setting():
	#存储《guess-a-number》中的设置的类
	
	def __init__(self):
		#产生随机的整数
		self.num = random.randint(1,101)
		#将判断条件初始设置为True
		self.switch = True
		self.begin =True
