p = int(input("Digite o primero termo: "))
rs = p
ra = int(input("Digite a razão: "))
pf = 10
while pf != 0:
    print('{} '.format(p), end="→ ")
    d = p + (pf - 1) * ra
    while p < d:
        p += ra
        print('{} '.format(p), end="→ ")
    p = rs
    print("END")
    pf = int(input("Digite quantos termos a mais voce quer: "))
print("Acabou!")

