import random
import time

def buscaVazio(m):
    for l in range(0,3):
        for c in range(0,3):
            if m[l][c] == 0:
                return l, c

def buscaEstados(m, l, c):
    abertos = []
    if l < 2:
        novoMovimento = [list(l) for l in m]
        novoMovimento[l][c], novoMovimento[l+1][c] = novoMovimento[l+1][c], 0
        abertos.append((novoMovimento, "Baixo"))
    if c < 2:
        novoMovimento = [list(l) for l in m]
        novoMovimento[l][c], novoMovimento[l][c+1] = novoMovimento[l][c+1], 0
        abertos.append((novoMovimento, "Direita"))
    if l > 0:
        novoMovimento = [list(l) for l in m]
        novoMovimento[l][c], novoMovimento[l-1][c] = novoMovimento[l-1][c], 0
        abertos.append((novoMovimento, "Cima"))
    if c > 0:
        novoMovimento = [list(l) for l in m]
        novoMovimento[l][c], novoMovimento[l][c-1] = novoMovimento[l][c-1], 0
        abertos.append((novoMovimento, "Esquerda"))
    return abertos

def buscaLargura():
    tempoInico = time.time()
    i = 0
    while abertos:
        estado, acoes = abertos.pop(0)
        i+=1
        visitados.append(estado)
        l, c = buscaVazio(estado)
        a = buscaEstados(estado, l, c)
        for elemento, acao in a:
            if elemento not in visitados:
                if elemento == obj:
                    tempoFim = time.time()
                    print("\nObjetivo alcançado em",i, "tentativas com um tempo de", tempoFim - tempoInico, "segundos")
                    print("Caminho de ações executadas:")
                    while acoes:
                        print(acoes.pop(0))
                    print("Estado final: ",elemento)
                    return
                abertos.append((elemento, acoes + [acao]))

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
abertos = [(estadoAtual, [])]

buscaLargura()
