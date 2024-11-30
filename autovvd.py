import numpy as np
import time as t
import os




matriz = np.array([
    [3, 1, 0, 2],
    [1, 4, 2, 0],
    [0, 2, 5, 1],
    [2, 0, 1, 6]
])


autovalores, autovetores = np.linalg.eig(matriz)
os.system('cls')
print("FALA PROFESSOR! DAVI E BRUNO AQUI.\nPRESSIONE ENTER PARA VER OS CALCULOS DE AUTOVALOR E AUTOVETOR DA MATRIZ A, ALÉM DA SUA DIAGONALIZAÇÃO!\n\n MATRIZ:\n{}".format(matriz))
input('PRESSIONE ENTER...')
os.system('cls')

print("Autovalores:")
print(np.round(autovalores, 2))

print("\nAutovetores:")
print(np.round(autovetores, 2))


matriz_diagonalizada = np.dot(np.dot(np.linalg.inv(autovetores), matriz), autovetores)

print("\nMatriz diagonalizada (D):")
print(np.round(matriz_diagonalizada, 2))
