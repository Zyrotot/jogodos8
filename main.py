import random
import numpy as np

# Definindo meu objetivo
obj = np.reshape([1, 2, 3, 4, 5, 6, 7, 8, ""], (3,3))
print("Meu objetivo é:")
print(obj)

x = list(range(1,9)) # Criar uma lista com números entre 1 e 8

x.append("") # Adicionando valor vázio

random.shuffle(x) # Embaralhando a lista

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

##print(verificaObj(estadoAtual)) # Não é
##print(verificaObj(obj)) # é meu obj

# Buscando posição vázia na matriz
def buscaVazio(m):
    for l in range(0,len(m)):
        for c in range(0,len(m[l])):
            if m[l][c] == "":
                lc = [l, c]
                return lc #retorna linha e coluna do vázio na matriz

# Verifica Ações possíveis
def acoes(l, c):
    if l == 1:
        acaoLinha = [0, 2]
    else:
        acaoLinha = [1]
    if c == 1:
        acaoColuna = [0, 2]
    else:
        acaoColuna = [1]
    acoes = [acaoLinha, acaoColuna]
    return acoes

# Verifica estados que ações levam para filtrar com os visitados
def verificaVisitados(acaoL, acaoC, vazioL, vazioC):
##    print(acaoL, acaoC, vazioL, vazioC, "acaoL, acaoC, vazioL, vazioC")
    estadoAnteriorVerifica = estadoAtual
    estadoAtualVerifica = np.copy(estadoAtual)
    estadoAtualVerifica[acaoL][acaoC], estadoAtualVerifica[vazioL][vazioC] = estadoAtualVerifica[vazioL][vazioC], estadoAtualVerifica[acaoL][acaoC]
    i=0
    for v in range(0,len(visitados)):
        m = visitados[v]
##        print(m, "meu m")
        for l in range(0,3):
            for c in range(0,3):
                if estadoAtualVerifica[l][c] != m[l][c]:
                    print("(def verificaVisitados) Não é meu objetivo", m[l][c], " != ", estadoAtualVerifica[l][c])
                else:
                    i = i+1
                    if i == 9:
                        return i
    

# Movimentando
def movimenta(acaoL, acaoC, vazioL, vazioC, estadoAtual):
    estadoAnterior = np.copy(estadoAtual)
    estadoAtual = np.copy(estadoAtual)
    estadoAtual[acaoL][acaoC], estadoAtual[vazioL][vazioC] = estadoAtual[vazioL][vazioC], estadoAtual[acaoL][acaoC]
##    print(estadoAnterior, "estado anterior")
##    print(estadoAtual, "novo estado atual")
    return estadoAtual

# Percorre Acoes
def percorreAcoes(acoesL):
    for n in range(0,len(acoesL)): # percorre ações livres
        for k in range(0,len(acoesL[n])): # ações de linha e coluna
            if n == 0: # verifica ações de linha
                retAcoes = verificaVisitados(acoesL[n][k], lc[1], lc[0], lc[1])
##                print("passou daqui ", n, k, retAcoes)
                if retAcoes == 9:
##                    print("vou remover a ação: ", acoesL[n][k])
                    acoesL[n].remove(acoesL[n][k])
                    if len(acoesLivres[n]) > 0:
                           retAcoes = verificaVisitados(acoesL[n][k], lc[1], lc[0], lc[1])
                           if retAcoes == 9:
                               acoesL[n].remove(acoesL[n][k])
                           else:
                               novoEstado = movimenta(acoesL[n][k], lc[1], lc[0], lc[1], estadoAtual)
##                               print(novoEstado, "1")
                               return novoEstado
                else:
                    novoEstado = movimenta(acoesL[n][k], lc[1], lc[0], lc[1], estadoAtual)
##                    print(novoEstado, "2")
                    return novoEstado
            
            if n == 1: # verifica ações da coluna
                retAcoes = verificaVisitados(lc[0], acoesL[n][k], lc[0], lc[1])
                if retAcoes == 9:
                    acoesL[n].remove(acoesL[n][k])
                    if len(acoesLivres[n]) > 0:
                           retAcoes = verificaVisitados(lc[0], acoesL[n][k], lc[0], lc[1])
                           if retAcoes == 9:
                               acoesL[n].remove(acoesL[n][k])
                           else:
                               novoEstado = movimenta(lc[0], acoesL[n][k], lc[0], lc[1], estadoAtual)
##                               print(novoEstado, "3")
                               return novoEstado
                else:
                    novoEstado = movimenta(lc[0], acoesL[n][k], lc[0], lc[1], estadoAtual)
##                    print(novoEstado, "4")
                    return novoEstado


# -----> Busca em Amplitude = Custo Uniforme com custo unitário <-----
while 1:
    if verificaObj(estadoAtual) == 9:
        print("Parabéns você chegou no objetivo!!!")
        print(estadoAtual)
        break
    else: # Se o estadoAtual não solução
        abertos.remove(estadoAtual)
        visitados.insert(0,estadoAtual) ## POSSÍVEL AJUSTE AQUI
##        visitados.append(estadoAtual)        
    
    lc = buscaVazio(estadoAtual)
##    print("Lembrando que na matriz 3x3 a linha e coluna vão de 0 à 2")
    print("Posição do vázio [linha, coluna]: ", lc)
    acoesLivres = acoes(lc[0], lc[1]) ## ADICIONAR CUSTO
    print("Minhas ações disponíveis são: ")
    print("[ [açõesNaLinha], [açõesNaColuna] ]: ", acoesLivres)
    estadoAnterior = np.copy(estadoAtual)
    estadoAtual = percorreAcoes(acoesLivres)
    print("Realizou ação:")
    print(estadoAtual, " <-- meu novo estado!")
    print("Visitados:")
    print(visitados)
    print("Abertos:  <-- Preciso ajustar")
    print(abertos)
    break
        
