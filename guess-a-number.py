# -*- coding:utf-8 -*-
#猜数字游戏升级版

import pygame
import functions as f
from setting import Setting


def run_game():
	gn_settings = Setting()
	print('Let\'s begin the game!')
	#开始游戏主循环
	while gn_settings.begin:
		f.guess(gn_settings.num)
		f.go_on_game()
		
		

run_game()

