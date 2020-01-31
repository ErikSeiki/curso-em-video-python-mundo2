soma = 0
media = 0
mais_velho = 0
nome_mais_velho = ""
mulher_menor = 0
for a in range(0, 4):
    print("-"*10,"{}º pessoa".format(a+1),"-"*10)
    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))
    sexo = input("Sexo(F/M): ").upper().strip()
    soma = idade + soma
    if idade > mais_velho and sexo == "M":
        nome_mais_velho = nome
    if idade < 20 and sexo =="F":
        mulher_menor += 1
print()
media = soma / 4
print("A media de idade é {:.2f}".format(media))
print("O homem mais velho se chama {} e possui {}".format(nome_mais_velho.capitalize(),mais_velho))
print("Possui {} mulheres menores de 20 anos idade".format(mulher_menor))