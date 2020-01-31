n = int(input("Digite até qual termo voce quer: f"))
i = 0
x1 = 1
x0 = 0
while i != n + 1:
    if i % 2 == 0:
        print(end="f{}: {} → ".format(i,x0))
        x0 += x1
    else:
        print(end="f{}: {} → ".format(i,x1))
        x1 += x0
    i += 1

print("=-"*20)
n_atual = 1
n_anterior = 0
for t in range(1, n):
    print("termo", t, "valor", n_atual)
    n_anterior = n_atual - n_anterior
    n_atual = n_anterior + n_atual
