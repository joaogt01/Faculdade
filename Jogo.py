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
        armador -= 1
        andarilho -= 2
    elif opcaoJogador == 2:
        armador += 2
        andarilho += 1
        print(f"O armador é o jogador: {armador}")
        print(f"O andarilho é o jogador: {andarilho}")
        armador -= 2
        andarilho -= 1
    else:
        print("opçao invalida, tente novamente ")
def plantar_armadilhas():
    global armador
    matriz = [
        ['A','A','A','A','A'],
        ['A','A','A','A','A'],
        ['A','A','A','A','A'],
        ['A','A','A','A','A'],
        ['A','A','A','A','A']
    ]
    print(matriz)
    print(f'jogador {armador}, voce pode esconder ate 3 ovos podres por linha no terreno.')
    ovos = 0
    contador = 0
    while ovos < 15:
        for linha in range(1,6):
            print(f'em qual coluna da linha {linha} voce quer esconder ovos podres?')
            while contador < 3:
                entrada_ovos = int(input())
                podres.append(entrada_ovos)
                print('deseja colocar mais algum nessa coluna? [S/N]')
                a = input().upper()
                if a == 'S':
                    contador += 1
                elif a == 'N':
                    contador += 2
        print(podres)
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