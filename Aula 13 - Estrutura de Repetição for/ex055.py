maior = 0
menor = 0
x = 0
for c in range(0, 5):
    x = float(input("Digite o peso da {}º pessoa: ".format(c + 1)))
    if c == 1:
        maior = x
        menor = x
    else:
        if x > maior:
            maior = x
        elif x < menor:
            menor = x
print("O maior peso foi de {} Kg e o menor foi de {} Kg".format(maior, menor))
