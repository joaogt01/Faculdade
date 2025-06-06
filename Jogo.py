andarilho = 0
armador = 0
verdadeiro = 0
entrada = 0
podres = []
matriz = []
def placar():
    pontuacao1 = 0
    pontuacao2 = 0
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
    global armador, matriz
    matriz = []
    for i in range(5):
        linha = ['A'] * 5
        matriz.append(linha)
    print(f'Jogador {armador}, voce pode esconder até 3 ovos podres por linha do terreno.')
    for x in range(5):
        print(f'\nLinha {x + 1}:')
        ovos_na_linha = 0
        while ovos_na_linha < 3:
            try:
                coluna = int(input(f'Digite a coluna para esconder o ovo podre {ovos_na_linha + 1} [1-5]: ')) - 1
                if coluna < 0 or coluna > 4:
                    print('Coluna inválida! Digite um valor entre 1 e 5.')
                    continue
                if matriz[x][coluna] == 'O':
                    print('Já existe um ovo podre nesta posição!')
                    continue
                matriz[x][coluna] = 'O'
                ovos_na_linha += 1
                if ovos_na_linha < 3:
                    continuar = input('Deseja adicionar mais algum ovo nesta linha? [S/N] ').upper()
                    if continuar != 'S':
                        break
            except ValueError:
                print('Por favor, digite um número válido.')
    print('\nTerreno com as armadilhas:')
    for linha in matriz:
        print(linha)


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
        print(' ')
        for divisor in range(99):
            print('=' * divisor)
        espacos = [1, 2, 3, 4, 5]
        for linha in matriz:
            print(f'São validos os espaços: [{espacos}]')
            espacos.clear()
            print('Escolha sabiamente um dos espaços validos')
            escolha_espaco = int(input())
            if linha[escolha_espaco -1] == 'A':
                if escolha_espaco > 1:
                    espacos.append(escolha_espaco - 1)
                espacos.append(escolha_espaco)
                if escolha_espaco < 5:
                    espacos.append(escolha_espaco + 1)
                continue
            elif linha[escolha_espaco -1] == 'O':
                print("Eca! Voce pisou em um ovo podre e perdeu")
                break
            elif len(espacos) == 0:
                print("Voce atravessou o terreno sem cair em nenhuma armadilha! Parabens!")
    elif entrada == 4:
        print("Em Desenvolvimento!")
