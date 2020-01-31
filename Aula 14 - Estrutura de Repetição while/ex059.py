from time import sleep

x = int(input("Digite o 1º valor: "))
y = int(input("Digite o 2º valor: "))
print("=-"*20)
escolha = int(
    input("Escolha entre: \n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos valores\n[5] Sair do programa\n"))
print("=-"*20)
while escolha != 5:
    if escolha == 1:
        print("A soma foi de {}".format(x + y))
    elif escolha == 2:
        print("A multiplicação foi de {}".format(x * y))
    elif escolha == 3:
        if x > y:
            print("O numero {} é maior {}".format(x,y))
        elif x < y:
            print("O numero {} é maior {}".format(y,x))
        else:
            print("Ambos os numeros são iguais")
    elif escolha == 4:
        x = int(input("Digite o novo valor para o primeiro numero: "))
        y = int(input("Digite o novo valor para o segundo numero: "))
    else:
        print("Não ha esta opção!")
    print("=-"*20)
    sleep(2)
    escolha = int(input(
        "Escolha novamente entre: \n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos valores\n[5] Sair do programa\n"))
    print("=-"*20)
print("Voce acabou de sair so programa!")
