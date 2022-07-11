def cambiarValores(x, y):
	x = x + y
	y = x - y
	x = x - y
	return x, y

if __name__ == '__main__': 
	print(cambiarValores(67, 56))