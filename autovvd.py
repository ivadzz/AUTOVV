import numpy as np
import time as t
import os

matriz = np.array([
    [6,2,1,3],
    [0,5,0,0],
    [0,0,4,0],
    [0,0,0,3]
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
