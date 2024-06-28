# Cálculo de IMC, Declara o tipo de dados que o código vai receber com o print(type(s)),
# cálculo do imposto de um salário 


#Cálculo de IMC
peso=80
altura=1.80
IMC = ( peso / (altura *altura))
print
input
print("O seu IMC é: %.1f"%IMC)


# declara o tipo de dados que o código vai receber com o print(type(s))
idade=int(input("Digite sua idade: "))
print(type(idade))

#cálculo do imposto de um salário 
salario=int(input("Digite o Salario: "))
imposto=float(input("Digite o imposto: "))
vi=float(salario*(imposto/100))
valor=(salario)-(vi)
print("Valor total do imposto é: R$ %.2f"%vi)

