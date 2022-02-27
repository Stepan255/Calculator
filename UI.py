# Создание пользовательского интерфейса 

def view_data(data, title):
    print(f'{title} = {data}')

def get_value(title):
    return int(input(f'{title} = '))

def get_text(title):
    return input(f'{title} = ')

def get_sign():
	sign = input('input action: ')
	actions = '/*-+^#@'
	while sign not in actions:
		print('invalid value')
		sign = input('input action: ')
	return sign