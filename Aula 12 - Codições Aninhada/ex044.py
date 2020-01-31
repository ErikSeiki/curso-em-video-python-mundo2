p = float(input("Digite o valor do produto: R$ ").strip())
print(
    "Escolha a forma de pagamento\n-Dinheiro/Cheque (tem 10% de Desconto)\n-Cartão\n +1x (5% de desconto)\n +2x (preço normal)\n +3x ou mais (20% de juros)")
e = input("Sua escolha: ").strip()
if e.capitalize() == "Dinheiro" or e.capitalize() == "Cheque":
    d = p * (10 / 100)
    print("Deverá pagar R${:.2f}".format(p - d))
elif e.capitalize() == "Cartão":
    quant = int(input("Digite a quantidade de vezes: ").strip())
    if quant == 1:
        d = p * (5 / 100)
        print("Deverá pagar R${:.2f}".format(p - d))
    elif quant == 2:
        print("Deverá pagar R${:.2f} em 2x de R${:.2f}".format(p, p / 2))
    else:
        j = p * (20 / 100)
        print("Deverá pagar R${:.2f} em {}x de R${:.2f}".format(p + j, quant, (p + j) / quant))
else:
    print("Não a esta opção.")

print("-=-" * 20)
print()
print("{:^40}".format("Lojas Seiki"))
pn = float(input("Digite o valor do produto: R$ "))
print(
    "Escolha a forma de pagamento\n[1] Dinheiro/Cheque, tem 10% de Desconto\n[2] Cartão em 1x, tem 5% de desconto\n[3] Cartão em 2x,tem o preço normal\n[4] Cartão em 3x ou mais, tem 20% de juros")
en = int(input("Sua escolha: ").strip())
if en == 1:
    total = pn - (pn * 10 / 100)
elif en == 2:
    total = pn - (pn * 5 / 100)
elif en == 3:
    total = pn
    par = pn / 2
    print("Sua compra será parcelada em 2x de R${:.2f}".format(par))
elif en == 4:
    total = pn + (pn * 20 / 100)
    parc = int(input("Quantas parcelas são: "))
    par = pn / parc
    print("Sua compra será parcelada em {}x de R${:.2f} com juros".format(parc, par))
else:
    print("Opção invalida de pagamento tente novamento")
print("Sua compra de R${:.2f} vai custar  R${:.2f} no final".format(pn, total))
