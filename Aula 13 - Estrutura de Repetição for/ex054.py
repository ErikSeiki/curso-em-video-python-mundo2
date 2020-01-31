from datetime import date

t = date.today().year
maior = 0
menor = 0
for c in range(0, 7):
    a = int(input("o ano de nascimento da {}º pessoa: ".format(c + 1)))
    if t - a < 21:
        menor += 1
    else:
        maior += 1
print("Existe {} maiores de idade e {} menores de idade!".format(maior, menor))
