n = 0
contador = 0
maior = 0
menor = 0
soma = 0
while n != 99999:
    n = int(input("Digite um novo valor se quiser continuar, se não digite 99999: "))
    if n != 99999:
        contador += 1
        soma += n
        if contador == 1:
            maoir = n
            menor = n
        else:
            if n > maior:
                maior = n
            elif n < menor:
                menor = n
print("Media: {} \nMaior: {}\nMenor: {}".format(soma/contador, maior, menor))
