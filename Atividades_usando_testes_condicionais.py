
# 01
n1=int(input("Digite um Número: "))
n2=int(input("Digite outro Número: "))
if (n1>n2):
    print('O número maior é',n1) 
elif(n2>n1):
    print('O número maior é',n2)
else:
    print('Os números são iguais')

# 02
val1=int(input("Digite um valor inteiro: "))
if (val1>0):
    print('O valor é positivo') 
elif(val1<0):
    print('O valor é negativo')
else:
    print('O valor é neutro')

# 03
nota1=int(input("Digite a primeira nota: "))
nota2=int(input("Digite a segunda nota: "))
nota3=int(input("Digite a terceira nota: "))
nota4=int(input("Digite a quarta nota: "))
média=(nota1+nota2+nota3+nota4)/4
print("A sua média é",média)
if (média>=7):
    print('Você está aprovado!!') 
elif(média<6 and média>3):
    print('Você está de exame!!')
else:
    print('Você está reprovado!!')

# 04
salario=float(input("Digite o seu Salário: "))
if (salario<500 ):
    novosalario=salario+(salario*15/100)
    print(novosalario)
elif (salario>499 and salario<1001):
    novosalario=salario+(salario*10/100)
    print(novosalario)
else: 
    novosalario=salario+(salario*5/100)
    print(novosalario)

# 05
vc=(input("Digite a letra que deseja saber se é vogal ou consoante: "))
vc=vc.lower()
if (vc=="a" or vc=="e" or vc=="i" or vc=="o" or vc=="u"):
    print("A letra ({}) é vogal".format(vc))
else: 
    print("A letra é vogal")
    
# 06
nota1=int(input("Digite a primeira nota: "))
nota2=int(input("Digite a segunda nota: "))
média= (nota1+nota2)/2
if (média>=7 and média<9):
    print('Aprovado!!') 
elif(média<7):
    print('Reprovado!!')
else:
    print('Aprovado com Distinção!!')

# 07
num1=int(input("Digite um número: "))
num2=int(input("Digite outro número: "))
num3=int(input("Digite outro número: "))
if (num1>num2 and num1>num3):
    print("O número maior é o ({})".format(num1))
elif (num2>num1 and num2>num3):
    print("O número maior é o ({})".format(num2))
elif (num3>num1 and num3>num2):
    print("O número maior é o ({})".format(num3))

# 08
#print("O valor Total é: R$ %.2f"%vt)
p1=int(input("Digite o preço do produto 01: "))
p2=int(input("Digite o preço do produto 02: "))
p3=int(input("Digite o preço do produto 03: "))
if (p1<p2 and p1<p3):
    print("O produto 01 é o que deve ser comprado custando R${}".format(p1))
elif (p2<p1 and p2<p3):
    print("O produto 02 é o que deve ser comprado custando R${}".format(p2))
elif (p3<p1 and p3<p2):
    print("O produto 03 é o que deve ser comprado custando R${}".format(p3))

# 09
num1=int(input("Digite um número: "))
num2=int(input("Digite outro número: "))
num3=int(input("Digite outro número: "))
if (num1<num2 and num2<num3):
    print(num3, num2, num1)
elif (num2<num1 and num1<num3):
    print(num3, num1, num2)
elif (num3<num1 and num1<num2):
    print(num2, num1, num3)

# 11 
sal=float(input("Digite o seu salário: "))
if (sal<281):
    novosalario=sal+(sal*20/100)
    percent = 20
elif (sal>280 and sal<700):
    novosalario=sal+(sal*15/100)
    percent = 15
elif (sal>=700 and sal<1500):
    novosalario=sal+(sal*10/100)
    percent = 10
elif (sal>=1500):
    novosalario=sal+(sal*5/100)
    percent = 5

print("O salário antes do reajuste é: R$",sal)
print("O percentual de aumento foi de:",percent)
print("O valor do aumento foi: R$",novosalario-sal)
print("O novo salário, após o aumento é: R$",novosalario)

#12 / terminar

vh=float(input("Digite o valor da sua hora: "))
ht=int(input("Digite a quantidade de horas trabalhadas no mês: "))
mult=vh*ht
if (mult<900):
    print("Isento de imposto!!")
elif(mult<1501 and mult>900):
    imp=mult+(mult*5/100)
    percent = 5
    

#25
tel=(input("Telefonou para a vítima? "))
lc=(input("Esteve no local do crime? "))
mora=(input("Mora perto da vítima? "))
devia=(input("Devia para a vítima? "))
tbl=(input("Já trabalhou com a vítima? "))

if tel == "sim" or tel =="Sim":
    print("ok")
elif lc == "sim" or lc =="Sim":
    print("Você é Suspeito(a) do crime ")
elif mora == "sim" or mora =="Sim":
    print("Você é Cúmplice do crime!!")
elif devia == "sim" or devia =="Sim":
    print("Você é Cúmplice do crime!!")
elif tbl == "sim" or tbl =="Sim":
    print("Você é inocente")
elif tbl == "sim" or tbl =="Sim":
    print("Você é inocente")


