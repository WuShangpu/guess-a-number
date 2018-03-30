# -*- coding:utf-8 -*-
#²ÂÊı×ÖÓÎÏ·Éı¼¶°æ
import random
import time
import pygame
import functions as f
from setting import Setting


def run_game():
	gn_settings = Setting()
	print('Let\'s begin the game!')
	time.sleep(1)
	while begin:
		f.guess()
		print('Do you want to play agian?')
		

run_game()

