import rational_numbers as rn
import UI
import complex_numbers as cn
import logg as log

def button_click():
	numbers = get_numbers()
	sign = UI.get_sign()
	rn.init(numbers[0], numbers[1])
	result = do_calculations(sign)
	print(f'result = {result}')
	log.logger(f'{numbers[2]} operation: {numbers[0]} {sign} {numbers[1]} = {result}')


def get_numbers():
	user_type = input('input "R" or "com"')
	if user_type == 'R':
		return rational_input()
	elif user_type == 'com':
		return complex_input()

def rational_input():
	number_1 = UI.get_value('first number: ')
	number_2 = UI.get_value('second number: ')
	return (number_1, number_2, 'rational')

def complex_input():
	number_1 = number_to_complex()
	number_2 = number_to_complex()
	return (number_1, number_2, 'complex')

def number_to_complex():
	real = UI.get_value('real part of complex number: ')
	imaginary = UI.get_value('imaginary part of complex number: ')
	return cn.convert_to_complex(real, imaginary)

def do_calculations(sign):
	if sign == '*':
		return rn.multiply()
	elif sign == '+':
		return rn.plus()
	elif sign == '-':
		return rn.minus()
	elif sign == '/':
		return rn.divide()
	elif sign == '^':
		return rn.degree()
	elif sign == '#':
		return rn.kor()