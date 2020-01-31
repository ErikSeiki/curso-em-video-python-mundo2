p = int(input("Digite o primero termo: "))
ra = int(input("Digite a razão: "))
d = p + (10 - 1) * ra
print('{} '.format(p), end="→ ")
while p < d:
    p += ra
    print('{} '.format(p), end="→ ")
print("END")