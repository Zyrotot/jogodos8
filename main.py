import random
import numpy as np

# Definindo meu objetivo
obj = np.reshape([1, 2, 3, 4, 5, 6, 7, 8, ""], (3,3))
print("Meu objetivo é:")
print(obj)

# x = list(range(1,9)) # Criar uma lista com números entre 1 e 8

# x.append("") # Adicionando valor vázio

# random.shuffle(x) # Embaralhando a lista
x = ["", 1, 2, 4, 5, 3, 7, 8, 6]
# Criando Matriz a partir da lista
estadoInicial = np.reshape(x, (3,3))
estadoAtual = estadoInicial
estadoAnterior = []
print("Matriz de estado inicial é:")
print(estadoAtual)

visitados = [] # Estados conhecidos
abertos = [estadoAtual]

# Verificando se o estado é meu objetivo
def verificaObj(m):
    i=0
    for l in range(0,3):
        for c in range(0,3):
            if m[l][c] != obj[l][c]:
                return i
            else:
                i = i+1
                if i == 9:
                    return i

# Buscando posição vázia na matriz
def buscaEstados(m):
    abertos = []
    for l in range(0,3):
        for c in range(0,3):
            copy = m.copy()
            if l < 2 and m[l+1][c] == "":
                copy[l+1][c] = copy[l][c]
                copy[l][c] = ""
                abertos.append(copy)
            elif c < 2 and m[l][c+1] == "":
                copy[l][c+1] = copy[l][c]
                copy[l][c] = ""
                abertos.append(copy)
            elif l > 0 and m[l-1][c] == "":
                copy[l-1][c] = copy[l][c]
                copy[l][c] = ""
                abertos.append(copy)
            elif c > 0 and m[l][c-1] == "":
                copy[l][c-1] = copy[l][c]
                copy[l][c] = ""
                abertos.append(copy)
    return abertos

# -----> Busca em Amplitude = Custo Uniforme com custo unitário <-----
while 1:
    state = abertos.pop(0)
    if verificaObj(state) == 9:
        print("Parabéns você chegou no objetivo!!!")
        print(state)
        break
    else: # Se o estadoAtual não solução
        for i in range(len(abertos)):
            if np.all(abertos[i] == state):
                abertos.pop(i)
                break
        visitados.append(state)

        a = buscaEstados(state)
        for elemento in a:
            if not any((elemento == v).all() for v in visitados):
                abertos.append(elemento)
                for i in abertos:
                    print(i)
