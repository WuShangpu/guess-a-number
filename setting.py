# -*- coding:utf-8 -*-
import random

class Setting():
	#�洢��guess-a-number���е����õ���
	
	def __init__(self):
		#���ж�������ʼ����ΪTrue
		self.begin =True
		self.switch = True
		self.num = random.randint(1,101)
