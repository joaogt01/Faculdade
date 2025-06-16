import random
import time
def menu_pokedex():
    print("-------------------")
    print('''Digite
1 para Listar Detalhes
2 para Apagar Registro
0 para voltar ao menu principal
Escolha uma ação:''')
    print("-------------------")
def menu():
    print("--------------------")
    print('''9 - Para abrir esse menu
8 - Subir
2- Descer
4 - Ir para esquerda
6 - Ir para direta
5 - Abrir Pokedex
0 - Sair do Jogo''')
    print("--------------------")
def grama(a):
    if a == "G":
        pokemon_selvagem = random.randint(0,1)
        capturado = {'pokemon': random.choice(pokemons), 'atributos': atributo()}
        if pokemon_selvagem == 1:
            print("Um pokemon selvagem apareceu!\nCapturar ou correr? [1-Capturar ou 2-Correr]")
            cap_correr = int(input())
            if cap_correr == 1:
                if capturado not in pokedex:
                    pokedex.append(capturado)
                    print("Pokemon Capturado!")
                    
            elif cap_correr == 2:
                print("Fujão!")
def atributo():
    lista_atributos = []
    for i in range(6):
        lista_atributos.append(random.randint(0,100))
    hp = "HP",lista_atributos[0]
    atk = "Atk",lista_atributos[1]
    deff = "Def",lista_atributos[2]
    sp_atk = "Sp atk",lista_atributos[3]
    sp_def = "Sp def",lista_atributos[4]
    speed = "Speed",lista_atributos[5]
    return hp,atk,deff,sp_atk,sp_def,speed
l = 19
c = 6
campo = [['A','A','A','A','A',' ',' ','A','A','A','A','A'],
        ['A',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','A'],
        ['A',' ',' ',' ','A',' ',' ',' ',' ',' ',' ','A'],    
        ['A','E','E','E','A','E','E','E','G','G','G','A'],    
        ['A',' ',' ',' ','A','G','G','G','G','G','G','A'],    
        ['A','E','E','E','A','G','G','G','G','G','G','A'],    
        ['A',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','A'],
        ['A',' ',' ',' ',' ',' ',' ',' ','G','G','G','A'],
        ['A','A','E','E','E','A','A','A','G','G','G','A'],
        ['A',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','A'],
        ['A','E',' ','E','E',' ','E','E','E','E','E','A'],
        ['A',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','A'],
        ['A',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','A'],
        ['A','A','A','A','A','A','G','G','G','E','E','A'],
        ['A',' ',' ',' ',' ',' ','G','G','G',' ',' ','A'],
        ['A',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','A'],
        ['A','E','E',' ',' ','E','E','E','E','E','E','A'],
        ['A',' ','G','G','G','G',' ',' ','G','G','G','A'],
        ['A','G','G','G',' ',' ',' ','G','G','A','A','A'],
        ['A','A','A','A','A','A','G','A','A','A','A','A']]
pokemons = ['ratata', 'pidgey', 'weedle', 'caterpie', 'paras', 'charmander', 'bulbasaur', 'squirtle', 'pikachu' , 'evee']
pokedex = []
jogador = campo[19][6]

print("entrando na rota 1")
time.sleep(2)
for linha in campo:
    print(linha)
while True:
    print(f"Sua posição no mapa é: linha {l}, coluna {c}")
    time.sleep(1)
    menu()
    entrada = int(input())
    if entrada == 9:
        continue

    elif entrada == 8:
        l -= 1
        jogador = campo[l][c]
        if jogador == "A":
            print("Bump!")
            l += 1
        elif jogador == "G":
            grama(jogador)
        elif l < 0 or l > 19:
            print("Fim de jogo")
            break
        elif jogador == "E" and campo[l + 1][c] != "E":
            print("Bump!")
            l += 1
        else:
            print(jogador)

    elif entrada == 2:
        l += 1
        jogador = campo[l][c]
        if jogador == "A":
            print("Bump!")
            l -= 1
        elif jogador == "G":
            grama(jogador)
        elif l < 0 or l > 19:
            print("Fim de jogo")
            break
        else:
            print(jogador)
            print("-----")

    elif entrada == 4:
        c -= 1
        jogador = campo[l][c]
        if jogador == "A":
            print("Bump!")
            c+=1
        elif jogador == "G":
            grama(jogador)
        else:
            print(jogador)
            print("-----")           

    elif entrada == 6:
        c += 1
        jogador= campo[l][c]
        if jogador == "A":
            print("Bump!")
            c-=1
        elif jogador == "G":
            grama(jogador)
        else:
            print(jogador)

    elif entrada == 5:
        print("Pokémons capturados:")
        for p in pokedex:
            print(f"{p['pokemon']}")
        while True:
            menu_pokedex()
            opcao_pokedex = int(input())
            if opcao_pokedex == 0:
                break
            elif opcao_pokedex == 1:
                consultar_atributo = input("Digite o pokemon a ser consultado:").lower()
                for registro in pokedex:
                    if registro['pokemon'] == consultar_atributo:
                        print(registro['atributos'])
            elif opcao_pokedex == 2:
                consultar_atributo = input("Digite o pokemon a ter o registro apagado:").lower()
                for registro in pokedex:
                    if registro['pokemon'] == consultar_atributo:
                        pokedex = [p for p in pokedex if p['pokemon'] != consultar_atributo]

    elif entrada == 0:
        break
    else:
        print("Entrada Invalida, Tente Novamente")
        continue