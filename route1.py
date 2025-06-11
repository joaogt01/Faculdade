import random
import time
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
        if pokemon_selvagem == 1:
            print("Um pokemon selvagem apareceu!\nCapturar ou correr? [1-Capturar ou 2-Correr]")
            cap_correr = int(input())
            if cap_correr == 1:
                pokedex.append(random.choice(pokemons))


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

pokemons = [ 'Ratata', 'Pidgey', 'Weedle', 'Caterpie', 'Paras', 'Charmander', 'Bulbasaur', 'Squirtle', 'Pikachu' , 'Evee' ]
pokedex = []
jogador = campo[19][6]
print("entrando na rota 1")
time.sleep(3)
while True:
    print(f"Sua posição no mapa é: linha {l}, coluna {c}")
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
        else:
            print(jogador)
        print("-----")
    elif entrada == 2:
        l += 1
        jogador = campo[l][c]
        if jogador == "A":
            print("Bump!")
            l -= 1
        else:
            print(jogador)
            print("-----")
    elif entrada == 4:
        c -= 1
        jogador = campo[l][c]
        if jogador == "A":
            print("Bump!")
            c+=1
        else:
            print(jogador)
        print("-----")
    elif entrada == 6:
        c += 1
        jogador= campo[l][c]
        if jogador == "A":
            print("Bump!")
            c-=1
        else:
            print(jogador)
        print("-----")
    elif entrada == 5:
        print("5")
    elif entrada == 0:
        break
    else:
        print("Entrada Invalida, Tente Novamente")
        continue