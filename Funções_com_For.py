for i in range(11):
    print(i)# faz uma Ordem Crescente do 0 ao num anterior ao do()

for data in range(1995,2018):
    print(data)# faz uma Ordem Crescente de um número a outro

paises = ['China', 'Índia', 'Tailândia']
for pais in paises:
    print(pais)
    if pais == "Índia":
        break

paises = ['Pedro', 'João','Leticia']
for pais in paises:
    print(pais)
    if pais == "João":
        break 

# calculadora de 1 a 10 com o For 
for i in range (1,11):
    for j in range (1,11):
     print(i, "X", j, "=", i*j)
print('\n')

# imprime os números impares 
for i in range (1,51):
     if (i%2==1):
        print(i)

num=int(input(" Digite um número inteiro: "))
num2=int(input(" Digite outro número inteiro: "))
z=0
for i in range(num,num2+1):
    print(i)
    z=z+i
print('A soma total dos números é: ',z)

for i in range(1,21):
    print(i, end=" ")

# arrumar for i in range (1,6):
n1=int(input("Digite o primeiro número : "))
n2=int(input("Digite o segundo número: "))
n3=int(input("Digite o terceiro número: "))
n4=int(input("Digite o quarto número: "))
n5=int(input("Digite o quinto número: "))
soma=n1+n2+n3+n4+n5
print("A soma dos números é:",soma)
media=(n1+n2+n3+n4+n5)/5
print("A média dos números é:",media)


x=int(input("Digite um número inteiro que deseja fatorar: "))
fact=1
for i in range(1,x+1):
    fact=fact*i
    print(fact)