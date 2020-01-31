valor_casa = float(input("Digite o valor da casa a ser comprada: R$ "))
salario = float(input("Digite o valor do seu salario: R$"))
quant_anos_pagamento = int(input("Digite a quantidade de anos que voce vai pagar: "))
quant_mes_pagamento = quant_anos_pagamento * 12
pagamento_mensal = valor_casa / quant_mes_pagamento
minimo_que_recebe_mensalmente = salario * 30 / 100
print("Voce deve pagar em {} meses".format(quant_mes_pagamento))
print("Quantos voce deve pagar por mes R${:.2f}".format(pagamento_mensal))
print("Minimo que voce pode pagar mensalmente é de R${:.2f}".format(minimo_que_recebe_mensalmente))
if pagamento_mensal > minimo_que_recebe_mensalmente:
    print("Não é possivel pagar essa casa")
else:
    print("É possivel comprar essa casa")
