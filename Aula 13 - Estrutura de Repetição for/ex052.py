num = int(input('Digite um numero: '))
z = 0
for c in range(1, num + 1):
    div = num % c
    if div == 0:
        z += 1
if z == 2:
    print("O numero {} é primo.".format(num))
else:
    print("O numero {} não é primo".format(num))

print("=-" * 30)

tot = 0
n = int(input("Digite um numero: "))
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end="")
        tot += 1
    else:
        print('\033[31m', end="")
    print("{} ".format(c), end="")
print("\n\033[0mO numero {} foi divisivel {} vezes".format(n,tot))
if tot == 2:
    print("E por isso ele é primo!")
else:
    print("E por isso ele não é primo!")