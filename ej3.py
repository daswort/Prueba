def buscarPosicion(lista, elem):
	i = 0
	for x in lista:
		if x == elem:
			return i
		i += 1

if __name__ == '__main__': 
	lista = [33, 345, 577, 5144, 5453, 55677, 767699]
	elem = 5144
	print(buscarPosicion(lista, elem))