def hello():
    print("olá !!!")
hello()

def hello(nome):
    print("Seja bem vindo",nome)
a=input("Digite seu nome: ")
hello(a)

def hello(nome,idade):
    print("Olá",nome,'\nSua idade é:',idade)
hello("Kauã",18)

def calcular_pagamento(qtd_horas,valor_hora):
    horas=float(qtd_horas)
    taxa=float(valor_hora)
    if horas<=40:
        salario=horas*taxa
    else:
        h_excd=horas-40
        salario=40*taxa+(h_excd*(1.5*taxa))
        print(salario)


def soma(x,y):
    result=x+y
    return result
a=int(input("Primeiro número: "))
b=int(input("Segundo número: "))
res=soma(a,b)
print("A soma dos números informados é:",res)


def inverte(nome,sobrenome):
    nomeInverso=sobrenome+' '+nome
    return nomeInverso
nome=input("Nome:")
sobrenome=input("Sobrenome:")
invertido=inverte(nome,sobrenome)
print("Olá",invertido)


def par(x):
    if(x%2)==0:
        return True
    else:
        return False
    
    
while True:
    num=int(input("Insira um número: "))
    if par(num):
        print("O número informado é Par")
    else:
        print("o número informado é impar")