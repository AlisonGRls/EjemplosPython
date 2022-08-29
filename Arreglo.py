from tkinter import N


numeros = []
numeros.append(3)
numeros.append(8)
numeros.append(9)
numeros.append(20)
print("elementos del arreglo:", *numeros)
numeros.insert(1, 15)
print("elementos del arreglo:", *numeros)
numeros.remove(3)
print("elementos del arreglo:", *numeros)