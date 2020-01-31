n = 0
c = 0
d = 0
while n != 999:
    n = int(input("Digite um valor:"))
    if n != 999:
        c += n
        d += 1
print("Voce digitou {} numeros e a soma foi de {}".format(d, c))
