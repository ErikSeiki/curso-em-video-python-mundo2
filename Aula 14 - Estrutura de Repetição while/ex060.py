n = int(input("Digite o numero: "))
m = 1
while n != 0:
    m *= n
    n -= 1
print(m)


n = int(input("Digite o numero: "))
m = n
while n != 1:
    n -= 1
    m *= n
print(m)
