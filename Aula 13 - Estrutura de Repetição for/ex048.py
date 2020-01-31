s = 0
n = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        n += 1
print("São {} numeros multiplos por 3 e impar e sua soma é {}".format(n, s))
