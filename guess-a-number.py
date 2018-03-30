# -*- coding:utf-8 -*-
#²ÂÊı×ÖÓÎÏ·Éı¼¶°æ
import random
import time
import pygame
from functions import *

num = random.randint(1,101)
print(num)

print('Let\'s begin the game!')
time.sleep(1)


begin =True

while begin:
	guess()
	
	print('Do you want to play agian?')

