from random import randint
from time import sleep

v = 0
d = 0
em = 0
while v < 4:
    print("Voce ira enfretar um oponente forte agora, o seu proprio computador!")
    e = input("Escolha entre,\n\033[31mPedra\033[m\n\033[33mPapel\033[m\n\033[34mTesoura\033[m\n")
    c = randint(1, 3)
    j = 0
    print()
    if e.upper() == "PEDRA":
        e = "\033[31mPedra\033[m"
        j = 1
    elif e.upper() == "PAPEL":
        e = "\033[33mPapel\033[m"
        j = 2
    elif e.upper() == "TESOURA":
        e = "\033[34mTesoura\033[m"
        j = 3
    else:
        print("\033[30mNão tem essa escolha!\033[m")
    print("JO")
    sleep(0.5)
    print("KEN")
    sleep(0.5)
    print("PO")
    sleep(0.2)
    print()
    if j != 0:
        print("Sua escolha {}".format(e))
        ce = ""

        if c == 1:
            ce = "\033[31mPedra\033[m"
        elif c == 2:
            ce = "\033[33mPapel\033[m"
        elif c == 3:
            ce = "\033[34mTesoura\033[m"
        print("A minha escolha é {}".format(ce))
        print()
        if j == c:
            print("\033[35mEmpate\033[m")
            em = em + 1

        elif j == 1 and c == 2 or j == 2 and c == 3 or j == 3 and c == 1:
            print("\033[36mEu ganhei!\033[m")
            d = d + 1

        elif j == 1 and c == 3 or j == 2 and c == 1 or j == 3 and c == 2:
            print("\033[32mVoce ganhou!\033[m")

            v = v + 1
        print()
        print("\033[30mEu ganhei {}; Você ganhou {}; Empate:{}\033[m".format(d, v, em))
        print()
        sleep(5)


itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print("""Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura""")
jogador = int(input('Qual é a sua jogada? '))
print("JO")
sleep(0.5)
print("KEN")
sleep(0.5)
print("PO")
sleep(0.2)
print('-=' * 20)
print('O computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 20)
if computador == 0:
    if jogador == 0:
        print("Empate!")
    elif jogador == 1:
        print("Jogador Ganhou!")
    elif jogador == 2:
        print("Computador Ganhou!")
    else:
        print("Jogada Invaidade")
elif computador == 1:
    if jogador == 0:
        print("Computador Ganhou!")
    elif jogador == 1:
        print("Empate!")
    elif jogador == 2:
        print("Jogador Ganhou!")
    else:
        print("Jogada Invaidade")

elif computador == 2:
    if jogador == 0:
        print("Jogador Ganhou!")
    elif jogador == 1:
        print("Computador Ganhou!")
    elif jogador == 2:
        print("Empate!")
    else:
        print("Jogada Invaidade")
