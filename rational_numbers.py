# import math


a = 0
b = 0
def init(number_1, number_2):
	global a
	global b
	a = number_1
	b = number_2

def plus():
	return a + b

def minus():
	return a - b

def multiply():
	return a * b

def divide():
	return a / b

def degree():
	# return math.degrees(a, b)
	return a ** b

def kor(a, b):
	return a ** (1/b)


