# como chamar uma biblioteca? 
#digite: import e a biblioteca

import os

nome = input('Digite o seu nome: ')
os.system('cls')# limpa tudo que está acima e printa o que vem abaixo 
print("O seu nome está certo?",nome)
os.system('pause')# pausa o programa e tocando em qualquer tecla continua
os.system('cls')

import math
q=float(input("Digite um número quebrado: "))
print(math.ceil(q))# mostra o num int mais próximo 

import math
x=-3
print(math.fabs(x))
x=3
print(math.factorial(x))# fatorar um número 

import math
y=3.5
print(math.floor,(y))# aredonda para o menor valor anterior

import math 
x=81
print(math.isqrt(x))# retorna a raiz quadrada do inteiro não negativo 

x=2
y=10 
print(math.pow(x,y))# retorna x elevado a potência de y

import datetime
print(datetime.date.today().strftime('%d/%m/%Y'))# printa a data que está no pc
print(datetime.datetime.now().strftime('%d/%m/%Y %H:%M'))# printa a data e a hora que está no pc


import time
a=0
x=time.perf_counter()
while a<10000:
    print (a)
    a+=1
y=time.perf_counter()
print(y-x)