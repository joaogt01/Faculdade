import random
import time
def rodada():
    print('''
Escolha uma das opcoes abaixo: 
1 - mover
2 - ajustar angulo
3 - disparar
0 - encerrar turno''')
def verificar_jogador():
    if personagens == 0:
        print("Configure os personagens antes de iniciar a partida")
    elif personagens == 1:
        return
def atributos():
    m = random.randint(10,20)
    a = random.randint(30,120)
    d = random.choice([1,-1])
    p = random.randint(0,69)
    v = random.randint(0,5)
    atributo = {'municao': m , 'angulo' : a, 'direcao' : d ,'posicao': p , 'velocidade' : v ,'combustivel': 10}
    return atributo
def menu():
    print('''VERMES DE GUERRA
Escolha uma das opções abaixo:
1 - Configurar
2 - Iniciar a partida
0 - Sair''')
def mapa():
    l = 6
    c = 70
    matriz = []
    for i in range(l):
        linha = []
        for j in range(c):
            linha.append('X')
        matriz.append(linha)
    matriz[0] = [''] * c
    matriz[1] = [''] * c
    matriz[2] = [''] * c
    matriz[3] = [''] * c
    for linha in matriz:
        print(linha)
personagens = 0
laco_jogo = True
while laco_jogo == True:
    menu()
    opcao = int(input())
    if opcao == 1:
        nick1 = input("Digite o nick do jogador 1: ")
        nick2 = input("Digite o nick do jogador 2: ")
        jogador1 = [nick1,atributos()]
        jogador2 = [nick2, atributos()]
        print(jogador1)
        print(jogador2)
        personagens += 1
    elif opcao == 2:
        verificar_jogador()


    elif opcao == 0:
        print("Desligando...")
        time.sleep(2)
        laco_jogo = False
    else:
        laco_jogo = False