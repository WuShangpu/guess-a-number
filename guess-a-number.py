# -*- coding:utf-8 -*-
#��������Ϸ������

import pygame
import functions as f
from setting import Setting


def run_game():
	gn_settings = Setting()
	print('Let\'s begin the game!')
	#��ʼ��Ϸ��ѭ��
	while gn_settings.begin:
		f.guess(gn_settings.num)
		f.go_on_game()
		
		

run_game()

