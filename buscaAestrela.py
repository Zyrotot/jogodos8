import random
import time

def buscaVazio(m):
    for l in range(0,3):
        for c in range(0,3):
            if m[l*3+c] == 0:
                return l, c

def buscaEstados(m, l, c):
    abertos = []
    if l < 2:
        novoMovimento = m.copy()
        novoMovimento[l*3+c], novoMovimento[(l+1)*3+c] = novoMovimento[(l+1)*3+c], novoMovimento[l*3+c]
        abertos.append((novoMovimento, "Baixo", heuristicaDistancia(novoMovimento, obj)))
    if c < 2:
        novoMovimento = m.copy()
        novoMovimento[l*3+c], novoMovimento[l*3+(c+1)] = novoMovimento[l*3+(c+1)], novoMovimento[l*3+c]
        abertos.append((novoMovimento, "Direita", heuristicaDistancia(novoMovimento, obj)))
    if l > 0:
        novoMovimento = m.copy()
        novoMovimento[l*3+c], novoMovimento[(l-1)*3+c] = novoMovimento[(l-1)*3+c], novoMovimento[l*3+c]
        abertos.append((novoMovimento, "Cima", heuristicaDistancia(novoMovimento, obj)))
    if c > 0:
        novoMovimento = m.copy()
        novoMovimento[l*3+c], novoMovimento[l*3+(c-1)] = novoMovimento[l*3+(c-1)], novoMovimento[l*3+c]
        abertos.append((novoMovimento, "Esquerda", heuristicaDistancia(novoMovimento, obj)))
    return abertos

def heuristicaDistancia(estadoAtual, obj):
    distancia = 0
    for i in range(3):
        for j in range(3):
            valor = estadoAtual[i*3+j]
            if valor != 0:
                linhaObj, colunaObj = buscaPosicao(obj, valor)
                distancia += abs(i - linhaObj) + abs(j - colunaObj)
    return distancia

def buscaPosicao(m, valor):
    for l in range(3):
        for c in range(3):
            if m[l*3 +c] == valor:
                return l, c

def buscaAEstrela(abertos, visitados):
    tempoInicio = time.time()
    i = 0
    while abertos:
        estado, acoes, custo = abertos.pop(0)
        i += 1
        visitados.append(estado)
        l, c = buscaVazio(estado)
        a = buscaEstados(estado, l, c)
        for elemento, acao, custo in a:
            if elemento not in visitados:
                if elemento == obj:
                    tempoFim = time.time()
                    tempo = tempoFim - tempoInicio
                    print("\nObjetivo alcançado em", i, "tentativas com um tempo de", tempo, "segundos")
                    print("Caminho de ações executadas:")
                    while acoes:
                        print(acoes.pop(0))
                    print("Estado final: ", elemento)

                    return i, tempo
                
                custoReal = len(acoes) + 1
                custoEstimado = custo
                custoTotal = custoReal + custoEstimado

                estadoExiste = None

                for s in abertos:
                    if s[0] == elemento:
                        estadoExiste = s
                        break
                if estadoExiste is None:
                    abertos.append((elemento, acoes + [acao], custoTotal))
                else:
                    if custoTotal < estadoExiste[2]:
                        abertos.remove(estadoExiste)
                        abertos.append((elemento, acoes + [acao], custoTotal))
        abertos.sort(key=lambda x: x[2])

def solutionAestrela(x):
    estadoAtual = x.copy()

    visitados = []
    abertos = [(estadoAtual, [], 0)]

    return buscaAEstrela(abertos, visitados)

obj = [1, 2, 3, 4, 5, 6, 7, 8, 0]