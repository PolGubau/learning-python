import numpy as np
import random

  
files = 5
columnes = 6
tauler = np.zeros((files, columnes))
tauler_visible= np.zeros((files, columnes))

for i in range(files): # omplir el tauler de mines
    for j in range(columnes):
        posar_mina = random.uniform(0, 1) # decimal del 0 al 1
        # print(posar_mina)
        if posar_mina > 2/3: # 2/3 de probabilitat de no posar mina
            tauler[i,j] = 1 # hi ha una mina

perdut = False
while not perdut:
    fila = int(input(f"Quina fila vols? (1-{files}), 0 per acabar: "))-1
    columna = int(input(f"Quina columna vols? (1-{columnes}), 0 per acabar: "))-1

    if fila == -1 or columna == -1:
        print("Joc acabat. Has perdut")
        perdut = True
    elif (fila < 0 or fila >= files) or (columna < 0 or columna >= columnes):
      print("Valor de fila i/o columnas incorrecte")
    
    else:
        print("Descobrint posició del tauler...")
        if tauler[fila, columna] == 1:
            print("Has trobat una mina! Has perdut")
            perdut = True
        else:
          fila_min = 0
          fila_max = files-1
          cols_min= 0
          cols_max= columnes-1

          if fila > 0:
            fila_min = fila-1
          if fila < files-1:
            fila_max = fila+1
          
          if columna > 0:
            cols_min = columna-1
          if columna < columnes-1:
            cols_max = columna+1

          num_mines = tauler[fila_min:fila_max+1, cols_min:cols_max+1].sum()

          tauler_visible[fila, columna] = num_mines
          print(f"No hi ha una mina. Hi ha {num_mines} mines al voltant")
          print(tauler_visible)
          