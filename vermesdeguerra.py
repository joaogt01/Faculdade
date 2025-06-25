import random
import math
import time
def menu():
    print('''\nVERMES DE GUERRA
Escolha uma das opções abaixo:
1 - Configurar
2 - Iniciar a partida
0 - Sair''')

def turno_menu():
    print('''\nTurno - Escolha uma das opções:
1 - Mover
2 - Ajustar ângulo
3 - Disparar
0 - Encerrar turno''')

def mapa(j1, j2):
    l = 6
    c = 70
    matriz = [[' ' for _ in range(c)] for _ in range(l)]
    for i in range(4, 6):
        matriz[i] = ['X'] * c
    matriz[3][j1['posicao']] = '<' if j1['direcao'] == -1 else '>'
    matriz[3][j2['posicao']] = '<' if j2['direcao'] == -1 else '>'
    for linha in matriz:
        print(''.join(linha))

def gerar_atributos(nick):
    return {
        'nick': nick,
        'municao': random.randint(10, 20),
        'angulo': random.randint(30, 120),
        'direcao': random.choice([-1, 1]),
        'posicao': random.randint(0, 69),
        'velocidade': random.randint(0, 5),
        'combustivel': 10
    }

def mover(verme):
    if verme['combustivel'] <= 0:
        print("Sem combustível!")
        return
    direcao = int(input("Mover para onde? 4 = Esquerda, 6 = Direita: "))
    if direcao == 4:
        if verme['posicao'] > 0:
            verme['posicao'] -= 1
            verme['direcao'] = -1
            verme['combustivel'] -= 1
        else:
            print("Não pode sair do mapa!")
    elif direcao == 6:
        if verme['posicao'] < 69:
            verme['posicao'] += 1
            verme['direcao'] = 1
            verme['combustivel'] -= 1
        else:
            print("Não pode sair do mapa!")

def ajustar_angulo(verme):
    while True:
        print(f"Ângulo atual: {verme['angulo']}")
        opc = int(input("8 = aumentar, 2 = diminuir, 0 = travar mira: "))
        if opc == 8 and verme['angulo'] < 120:
            verme['angulo'] += 1
        elif opc == 2 and verme['angulo'] > 30:
            verme['angulo'] -= 1
        elif opc == 0:
            break
        else:
            print("Comando inválido ou limite atingido.")

def disparar(atirador, alvo):
    if atirador['municao'] <= 0:
        print("Sem munição!")
        return
    alcance = (200 * math.sin(math.radians(2 * atirador['angulo']))) / 9.8
    alcance = round(alcance) * atirador['direcao']
    impacto = atirador['posicao'] + alcance
    atirador['municao'] -= 1
    if impacto == alvo['posicao']:
        print(f"Acertou {alvo['nick']}!")
        alvo['combustivel'] = 0
    elif 0 <= impacto <= 69:
        print(f"Projétil caiu na posição {impacto}.")
    else:
        print("O tiro saiu fora do mapa!")

def imprimir_atributos(j):
    print(
        f"Jogador {j['nick']} | Combustível: {j['combustivel']} | Munição: {j['municao']} | Ângulo: {j['angulo']}° | Direção: {'Esquerda' if j['direcao'] == -1 else 'Direita'} | Posição: {j['posicao']}")

personagens = 0
jogador1 = {}
jogador2 = {}

laco_jogo = True
while laco_jogo:
    menu()
    opcao = int(input(">> "))

    if opcao == 1:
        nick1 = input("Digite o nome do Jogador 1: ").strip()
        nick2 = input("Digite o nome do Jogador 2: ").strip()
        if not nick1 or not nick2:
            print("Nomes inválidos!")
            continue
        jogador1 = gerar_atributos(nick1)
        jogador2 = gerar_atributos(nick2)
        personagens = 1
        print("Personagens configurados!")

    elif opcao == 2:
        if personagens == 0:
            print("Configure os personagens antes de iniciar a partida.")
            continue

        atual, outro = (jogador1, jogador2) if jogador1['velocidade'] >= jogador2['velocidade'] else (
        jogador2, jogador1)

        while jogador1['combustivel'] > 0 and jogador2['combustivel'] > 0 and (
                jogador1['municao'] > 0 or jogador2['municao'] > 0):
            mapa(jogador1, jogador2)
            imprimir_atributos(atual)
            turno_menu()
            escolha = int(input(">> "))

            if escolha == 0:
                atual, outro = outro, atual
            elif escolha == 1:
                mover(atual)
            elif escolha == 2:
                ajustar_angulo(atual)
            elif escolha == 3:
                disparar(atual, outro)
                atual, outro = outro, atual
            else:
                print("Opção inválida!")

        print("\n--- Fim de Jogo ---")
        if jogador1['combustivel'] > jogador2['combustivel']:
            print(f"{jogador1['nick']} venceu com {jogador1['combustivel']} de combustível restante!")
        elif jogador2['combustivel'] > jogador1['combustivel']:
            print(f"{jogador2['nick']} venceu com {jogador2['combustivel']} de combustível restante!")
        else:
            print("Empate!")

    elif opcao == 0:
        print("Desligando...")
        time.sleep(1)
        laco_jogo = False
    else:
        print("Opção inválida!")
