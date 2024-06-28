
# Atividade 02-percentual de desconto e cálculo do valor total

Produto=(input("Digite o nome de um produto: "))
print((Produto))

quantidade=float(input("Digite a quantidade comprada: "))
print((quantidade))                                         

vu=float(input("Digite o valor unitário do produto : "))
print((vu))

percentual=float(input("Digite o percentual de desconto a ser aplicado: "))
print((percentual))

# Faz o cálculo do valor total e vê o percentual de desconto no produto escolhido

vt=float(quantidade*vu)

desconto=(vt)-(vt*percentual/100)
print("Valor total: R$ %.2f"%desconto)