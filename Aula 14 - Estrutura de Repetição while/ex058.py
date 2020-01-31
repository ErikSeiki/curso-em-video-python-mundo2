from random import randint

aleatorio = randint(0, 10)
contador = 1
escolha = int(input("Adivinhe o numero entre 0 ha 10: "))
while escolha != aleatorio:
    if escolha < 11 and escolha > -1:
        contador += 1
        if escolha < aleatorio:
            escolha = int(input("Mais!Tente novamente: "))
        elif escolha > aleatorio:
            escolha = int(input("Menos!Tente novamente: "))
    else:
        print("Não há esta opção")
        escolha = int(input("Tente novamente: "))
print("Parabens minha escolha foi {} voce adivinhou e tentou {}".format(aleatorio, contador))

print("-_-_-_" * 5, "Guanabara", "-_-_-_" * 5)
computador = randint(0, 10)
print("Sou seu computador... Acabei de pensar em um número entre 0 e 10.")
print("Será que você consegue adivinhar qual foi? ")
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite?'))
    palpites +=1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais... Tente mais uma vez.")
        elif jogador > computador:
            print("Menos... Tente mais uma vez." )
print("Acertou com {} tentativas. Parabéns!".format(palpites))

