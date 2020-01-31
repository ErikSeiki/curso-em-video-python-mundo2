a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))
if a > b:
    print("{} é maior que {}".format(a, b))
elif a < b:
    print("{} é menor que {}".format(a, b))
else:
    print("{} é igual a {}".format(a, b))
if a > b:
    print("O primeiro é maior")
elif a < b:
    print("O segundo é maior")
else:
    print("Ambos são iguais")
