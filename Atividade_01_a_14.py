#ex.01:
num=(input("Digite um número: "))
print(num)

#ex.02:
print("Alo mundo")

#ex.03:
n1=float(input("Digite o valor 01: "))
n2=float(input("Digite o valor 02: "))
total=n1+n2
print(total)

#ex.04:
n1=int(input("Digite a Nota 01: "))
n2=int(input("Digite a Nota 02: "))
n3=int(input("Digite a Nota 03: "))
n4=int(input("Digite a Nota 04: "))
media=(n1+n2+n3+n4)/4
print("A média dos números é:",media)

#ex.05:
m=float(input("Digite quantos metros deseja converter para centímetros: "))
cm=100
conv=m*cm
print("A medida em centimetros é =",conv,"cm")

#ex.06:
import math
raio = float(input("Digite o raio do círculo: "))
area = math.pi*raio**2
print(" A área do círculo é:",area)

#ex.07:
lado=float(input("Digite o lado do quadrado: "))
area = lado**2
print (" A área do quadrado é de", area)

#ex.08:
gh = float(input("Digite quantos você ganha por hora: "))
nht = float(input("Digite o número de horas trabalhadas: "))
total = gh*nht
print("O total do seu salário ao mês é: R$",total)

#ex.09:
temp=float(input("Digite a temperatura em graus Fahrenheit: "))
print((temp))
C=(5/9)*(temp-32)
print("A temperatura convertida é: %.2f"%C)

#ex.10:
num=int(input("Digite um número inteiro: "))
num2=int(input("Digite outro número inteiro: "))
nr= float(input("Digite um número real: "))
print(num,num2,nr)

#ex.11:
v1 = float(input("Digite o primeiro valor: "))
v2 = float(input("Digite o segundo valor: "))
v3 = float(input("Digite o terceiro valor: "))
p1 = (v1 * 2) * v2 / 2
p2 = (v1 * 3) + v3
p3 = v3 ** 3
print(p1, p2, p3)

#ex.12: 
alt=float(input("Digite a sua altura: "))
pi=(72.7*alt)-58
print(pi)

#ex.13:
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

#ex.14:
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