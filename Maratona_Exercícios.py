'''#ex 01
print ('Alo mundo')

#ex 02
num = input("informe um número: ")
print (" O número informado foi:",num)

#ex 03 
num1 = int(input("informe um número: "))
num2 = int(input("informe outro número: "))
soma=num1+num2
print (" A soma dos números informados é:",soma)

#ex 04
n1=int(input("Digite a Nota 01: "))
n2=int(input("Digite a Nota 02: "))
n3=int(input("Digite a Nota 03: "))
n4=int(input("Digite a Nota 04: "))
media=(n1+n2+n3+n4)/4
print("A média dos números é:",media)

#ex.05
m=float(input("Digite quantos metros deseja converter para centímetros: "))
cm=100
conv=m*cm
print("A medida em centimetros é =",conv,"cm")

#ex.06
raio = float(input("Digite o raio do círculo: "))
pi = 3.14
area = pi * raio ** 2
print("A área do círculo é: {:.2f}".format(area))

#ex.07
lado=float(input("Digite o lado do quadrado: "))
area = lado**2
print (" A área do quadrado é de", area)

#ex.08
gh = float(input("Digite quantos você ganha por hora: "))
nht = float(input("Digite o número de horas trabalhadas: "))
total = gh*nht
print("O total do seu salário ao mês é: R$",total)

#ex.09
temp=float(input("Digite a temperatura em graus Fahrenheit: "))
print((temp))
C=(5/9)*(temp-32)
print("A temperatura convertida é: %.2f"%C)

#ex.10
num=int(input("Digite um número inteiro: "))
num2=int(input("Digite outro número inteiro: "))
nr= float(input("Digite um número real: "))
print(num,num2,nr)

#ex.11
v1 = float(input("Digite o primeiro valor: "))
v2 = float(input("Digite o segundo valor: "))
v3 = float(input("Digite o terceiro valor: "))
p1 = (v1 * 2) * v2 / 2
p2 = (v1 * 3) + v3
p3 = v3 ** 3
print(p1, p2, p3)

#ex.12 
alt=float(input("Digite a sua altura: "))
pi=(72.7*alt)-58
print(pi)

#ex.13
h=float(input("Digite a sua altura: "))
sexo=(input("Digite o seu sexo: "))
masculino=(72.7*h)-58
feminino=(62.1*h)-44.7
if sexo == "masculino":
    print("Peso ideal:",masculino)
elif sexo == "feminino":
    print("Peso ideal:",feminino)
else:
    print("Variavel inválida")

#ex.14
limite=50
multa=4
peso=float(input("Digite a quantidade de pescados: "))
excesso=peso-limite
cal=multa*peso-limite
if peso >50:
    excesso = peso - limite
    multa = 4* limite
    print("o Excesso é de pescados é:",excesso,"kg e o valor da multa é de: R$",cal)
else:   
   print("A quantidade está dentro do limite")

   
   Calcule e mostre o total do seu salário no referido mês, 

sabendo-se que são descontados 11% para o Imposto de Renda, 

8% para o INSS e 5% para o sindicato, faça um programa que nos dê: 

    salário bruto. 

    quanto pagou ao INSS. 

    quanto pagou ao sindicato. 

    o salário líquido. 

calcule os descontos e o salário líquido, conforme a tabela abaixo: 

 

    + Salário Bruto : R$ 

    - IR (11%) : R$ 

    - INSS (8%) : R$ 

    - Sindicato ( 5%) : R$ 

    = Salário Liquido : R$ 

 

Obs.: Salário Bruto - Descontos = Salário Líquido. '''
#ex.15
imposto_renda=11
inss=8
sindicato=5
ganho_hora = float(input("\nDigite quantos você ganha por hora: "))
numero_horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))
salario_bruto = ganho_hora*numero_horas_trabalhadas
print("O total do seu salário ao mês é: R$",salario_bruto)
salario=salario_bruto*(imposto_renda/100)
print("Valor total do Imposto de Renda é: R$ %.2f"%salario)

imposto_inss=salario_bruto*(inss/100)
print("Valor total do inss é: R$ %.2f"%imposto_inss)

imposto_sindicato=salario_bruto*(sindicato/100)
print("Valor total pago ao Sindicato é: R$ %.2f"%imposto_sindicato)

salario_liquido=salario_bruto-salario-imposto_inss-imposto_sindicato
print("\nO salário líquido é:",salario_liquido)
#impostos_total=

# salario=int(input("Digite o Salario: "))
# imposto=float(input("Digite o imposto: "))
# vi=float(salario*(imposto/100))
# valor=(salario)-(vi)
# print("Valor total do imposto é: R$ %.2f"%vi)