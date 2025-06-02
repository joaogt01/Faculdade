andarilho = 0
armador = 0
verdadeiro = 0
entrada = 0
podres = []

def menu():
    print('------------------------------')
    print(''' 1 - Definir Armador         
 2 - Plantar Armadilhas     
 3 - Iniciar com Andarilho   
 4 - Mostrar o placar        
 0 - Finalizar o Jogo       ''')
    print('------------------------------')
def validar_entrada():
    global entrada
    opcoes = [0,1,2,3,4]
    entrada = int(input())
    while entrada not in opcoes:
        print("Opção Inválida, tente novamente!")
        entrada = int(input())
    return entrada
def armado():
    global armador, andarilho
    print('Qual jogador plantará as armadilhas? [1 ou 2]')
    opcaoJogador = int(input())
    if opcaoJogador == 1:
        armador += 1
        andarilho += 2
        print(f"O armador é o jogador: {armador}")
        print(f"O andarilho é o jogador: {andarilho}")

    elif opcaoJogador == 2:
        armador += 2
        andarilho += 1
        print(f"O armador é o jogador: {armador}")
        print(f"O andarilho é o jogador: {andarilho}")

    else:
        print("opçao invalida, tente novamente ")

def plantar_armadilhas():
    global armador
    matriz = []
    ovos = []
    for i in range(1,6):
        linha = []
        for j in range(1,6):
            linha.append('A')
        matriz.append(linha)
    for linha in matriz:
        print(linha)
    print(f'Jogador {armador}, voce pode esconder até 3 ovos podres por linha do terreno.')
    for x in range(1,6):
        for k in range(3):
            ovos_podres = int(input(f'Em qual coluna da linha {x} voce quer esconder os ovos podres? [1 a 5]'))
            ovos.append([{'coluna' : x, 'ovos' : ovos_podres}])
            print('Deseja adicionar mais algum ovo nessa linha? [S/N]')
            ovos_linha = input().upper()
            if ovos_linha == 'S':
                continue
            elif ovos_linha == 'N':
                break
    for linha in matriz:
        print(linha)
    print(ovos)





while verdadeiro == 0:
    menu()
    validar_entrada()
    if entrada == 0:
        print("Jogo finalizado")
        verdadeiro += 1
    elif entrada == 1:
        armado()
    elif entrada == 2:
        plantar_armadilhas()
    elif entrada == 3:
        print("Em Desenvolvimento!")
    elif entrada == 4:
        print("Em Desenvolvimento!")
