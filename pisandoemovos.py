def menu():
    print('''
Opções: 
1 - Definir Armador 
2 - Plantar Armadilhas 
3 - Iniciar com Andarilho 
4 - Mostrar o placar 
0 - Finalizar o Jogo
''')
armador = 0
andarilho = 0
matriz = []

def mapa():
    global matriz
    l = 5
    c = 5
    for valor1 in range(l):
        linha = []
        for valor2 in range(c):
            linha.append('A')
        matriz.append(linha)

    for linha in matriz:
        print(linha)
laco_jogo = True
while laco_jogo == True:
    menu()
    opcao_jogador = int(input())
    if opcao_jogador == 1:
        print('Qual jogador plantará as armadilhas? [1 ou 2]')
        jogador = int(input())
        if jogador == 1:
            armador = 1
            andarilho = 2
            print(f"o armador é o jogador {armador} e o andarilho é o jogador {andarilho}")
        elif jogador == 2:
            armador = 2
            andarilho = 1
            print(f"o armador é o jogador {armador} e o andarilho é o jogador {andarilho}")
    elif opcao_jogador == 2:
        mapa()
        print("plantar armadilhas")
    elif opcao_jogador == 3:
        print("Iniciar")
    elif opcao_jogador == 4:
        print("placar")
    elif opcao_jogador == 0:
        laco_jogo = False
    else:
        print('Opção Invalida, tente novamente!')
        continue