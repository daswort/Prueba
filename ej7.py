def imprimeCuadradoDeCeros(mapa):
    filas = len(mapa)
    columnas = len(mapa[0])
  
    sub_mapa = []
    for i in range(filas):
      temp = []
      for j in range(columnas):
        if i==0 or j==0:
          temp += mapa[i][j],
        else:
          temp += 0,
      sub_mapa += temp,

    for i in range(1, filas):
        for j in range(1, columnas):
            if (mapa[i][j] == 0):
                sub_mapa[i][j] = min(sub_mapa[i][j-1], sub_mapa[i-1][j], sub_mapa[i-1][j-1]) + 1
            else:
                sub_mapa[i][j] = 0

    s_grande = sub_mapa[0][0]
    i_grande = 0
    j_grande = 0
    for i in range(filas):
        for j in range(columnas):
            if (s_grande < sub_mapa[i][j]):
                s_grande = sub_mapa[i][j]
                i_grande = i
                j_grande = j
  
    print("El cuadrado de ceros más grande dentro de la matriz: ")
    for i in range(filas):
        for j in range(columnas):
            print (mapa[i][j], end = " ")
        print("")

    print('\n es: \n')

    for i in range(i_grande, i_grande - s_grande, -1):
        for j in range(j_grande, j_grande - s_grande, -1):
            print (mapa[i][j], end = " ")
        print("")
  
if __name__ == '__main__': 
    mapa = [[1, 0, 0, 1, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 0, 0, 1],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1]]
  
    imprimeCuadradoDeCeros(mapa)


       