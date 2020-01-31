n = str(input("Digite o seu nome: "))
if n == "Erik":
    print("Voce tem um nome bonito!")
elif n == "João" or n == "Maria":
    print("Seu nome é bem popular")
elif n in "Ana Fernanda Eliza Emily Alice":
    print("Voce tem um nome bem feminino")
else:
    print("Seu nome é bem normal")
print("Tenha um bom dia {}!".format(n))
