# -*- coding:utf-8 -*-
#猜数字大小的函数


def guess():
	switch = True
	while switch:
		ans = int(input('Please input a number:'))
		if ans > num:
			print('Too big!')
			switch = True
		elif ans < num:
			print('Too small!')
			switch = True
		else:
			print('Bingo!')
			switch = False
