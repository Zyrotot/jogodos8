import random
import time

def buscaVazio(m):
    abertos = []
    for l in range(0,3):
        for c in range(0,3):
            if m[l][c] == 0:
                return l, c

def buscaEstados(m, l, c):
    abertos = []
    if l < 2:
        new_m = [list(l) for l in m]
        new_m[l][c], new_m[l+1][c] = new_m[l+1][c], 0
        abertos.append(new_m)
    if c < 2:
        new_m = [list(l) for l in m]
        new_m[l][c], new_m[l][c+1] = new_m[l][c+1], 0
        abertos.append(new_m)
    if l > 0:
        new_m = [list(l) for l in m]
        new_m[l][c], new_m[l-1][c] = new_m[l-1][c], 0
        abertos.append(new_m)
    if c > 0:
        new_m = [list(l) for l in m]
        new_m[l][c], new_m[l][c-1] = new_m[l][c-1], 0
        abertos.append(new_m)

    return abertos

def buscaProfundidade():
    start = time.time()
    i = 0
    while 1:
        state = abertos.pop(0)
        i=i+1
        
        visitados.append(state)
        l, c = buscaVazio(state)
        a = buscaEstados(state, l, c)
        for elemento in a:
            if elemento not in visitados:
                if elemento == obj:
                    end = time.time()
                    print("\nObjetivo alcançado em",i, "tentativas com um tempo de", end - start, "segundos")
                    print(state)
                    return
                abertos.append(elemento)

def buscaAestrela():
    start = time.time()
    i = 0
    while 1:
        state = abertos.pop(0)
        i=i+1
        
        visitados.append(state)
        l, c = buscaVazio(state)
        a = buscaEstados(state, l, c)
        for elemento in a:
            if elemento not in visitados:
                if elemento == obj:
                    end = time.time()
                    print("Objetivo alcançado em",i, "tentativas!\n")
                    print(state)
                    return
                abertos.append(elemento)

obj = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
print("Meu objetivo é:")
print(obj)

# x = list(range(0,9))
# random.shuffle(x)

# x1 = x[:3]
# x2 = x[3:6]
# x3 = x[6:]

# x = [x1, x2, x3]

x = [[0, 5, 3], [7, 2, 6], [4, 1, 8]]

# x = [[0, 1, 2], [4, 5, 3], [7, 8, 6]]
# x = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

estadoAtual = x.copy()
print("Matriz de estado inicial é:")
print(estadoAtual)

visitados = []
abertos = [estadoAtual]

buscaProfundidade()
