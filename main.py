import random
import copy

# Definindo meu objetivo
obj = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
print("Meu objetivo é:")
print(obj)

x = list(range(0,9)) # Criar uma lista com números entre 1 e 8
random.shuffle(x) # Embaralhando a lista

x1 = x[:3]
x2 = x[3:6]
x3 = x[6:]

x = [x1, x2, x3]

# x = [[0, 1, 2], [4, 5, 3], [7, 8, 6]]
# x = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Criando Matriz a partir da lista
estadoAtual = x.copy()
print("Matriz de estado inicial é:")
print(estadoAtual)

visitados = [] # Estados conhecidos
abertos = [estadoAtual]

def buscaVazio(m):
    abertos = []
    for l in range(0,3):
        for c in range(0,3):
            if m[l][c] == 0:
                return l, c

def buscaEstados(m, l, c):
    abertos = []

    if l < 2:
        temp = copy.deepcopy(m)
        temp[l][c] = temp[l+1][c]
        temp[l+1][c] = 0
        abertos.append(temp)
    if c < 2:
        temp = copy.deepcopy(m)
        temp[l][c] = temp[l][c+1]
        temp[l][c+1] = 0
        abertos.append(temp)
    if l > 0:
        temp = copy.deepcopy(m)
        temp[l][c] = temp[l-1][c]
        temp[l-1][c] = 0
        abertos.append(temp)
    if c > 0:
        temp = copy.deepcopy(m)
        temp[l][c] = temp[l][c-1]
        temp[l][c-1] = 0
        abertos.append(temp)

    return abertos

print("\n")

i = 0
# -----> Busca em Amplitude = Custo Uniforme com custo unitário <-----
while 1:
    state = abertos.pop(0)
    i=i+1
    
    if state == obj:
        print("Parabéns você chegou no objetivo!!!")
        print(state, "em",i, "tentativas \n")
        break
    else:
        visitados.append(state)
        l, c = buscaVazio(state)
        a = buscaEstados(state, l, c)
        for elemento in a:
            if elemento not in visitados:
                abertos.append(elemento)
