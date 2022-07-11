def buscaCamino(c1, c2):
    mapa = [['O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'X', 'O', 'X', 'O', 'X'],
            ['O', 'O', 'O', 'X', 'O', 'O']]

    origen = {'fila': c1[0], 'columna': c1[1], 'distancia': 0}
    destino = {'fila': c2[0], 'columna': c2[1]}
 
    visitado = [[False for _ in range(len(mapa[0]))] for _ in range(len(mapa))]
    cola = []
    cola.append(origen)
    visitado[origen['fila']][origen['columna']] = True
    while len(cola) != 0:
        origen = cola.pop(0)
 
        # destino encontrado
        if (origen['fila'] == destino['fila'] and origen['columna'] == destino['columna']):
            return origen['distancia']
 
        # camino arriba
        if esCeldaValida(origen['fila'] - 1, origen['columna'], mapa, visitado):
            cola.append({'fila': origen['fila'] - 1, 'columna': origen['columna'], 'distancia': origen['distancia'] + 1})
            visitado[origen['fila'] - 1][origen['columna']] = True
 
        # camino abajo
        if esCeldaValida(origen['fila'] + 1, origen['columna'], mapa, visitado):
            cola.append({'fila': origen['fila'] + 1, 'columna': origen['columna'], 'distancia': origen['distancia'] + 1})
            visitado[origen['fila'] + 1][origen['columna']] = True
 
        # camino a la izquierda
        if esCeldaValida(origen['fila'], origen['columna'] - 1, mapa, visitado):
            cola.append({'fila': origen['fila'], 'columna': origen['columna'] - 1, 'distancia': origen['distancia'] + 1})
            visitado[origen['fila']][origen['columna'] - 1] = True
 
        # camino a la derecha
        if esCeldaValida(origen['fila'], origen['columna'] + 1, mapa, visitado):
            cola.append({'fila': origen['fila'], 'columna': origen['columna'] + 1, 'distancia': origen['distancia'] + 1})
            visitado[origen['fila']][origen['columna'] + 1] = True
    return -1
 
 
# reviso si la celda a la que me muevo es valida (!= X)
def esCeldaValida(x, y, mapa, visitado):
    if ((x >= 0 and y >= 0) and
        (x < len(mapa) and y < len(mapa[0])) and
            (mapa[x][y] != 'X') and (visitado[x][y] == False)):
        return True
    return False
 
if __name__ == '__main__': 
    c1 = [0,0]
    c2 = [2,5]

    saltos = buscaCamino(c1, c2)
    mensaje = 'Camino encontrado' if (saltos != -1) else 'No se encontró camino'
    print(mensaje)