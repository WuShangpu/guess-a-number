# -*- coding:utf-8 -*-
from setting import Setting
import sys

f_settings = Setting()

#�ж��Ƿ������Ϸ
def go_on_game():
	if f_settings.switch == False:
		go = input('Do you want play agian? YES or NO? ')
		if go == 'YES' or 'yes':
			guess(f_settings.num)
		elif go == 'NO' or 'no':
			sys.exit()
		
	
		
#�����ִ�С�ĺ���
def guess(num):
	while f_settings.switch:
		ans = int(input('Please input a number:'))
		if ans > num:
			print('Too big!')
			f_settings.switch = True
		elif ans < num:
			print('Too small!')
			f_settings.switch = True
		else:
			print('Bingo!')
			f_settings.switch = False
			

	
