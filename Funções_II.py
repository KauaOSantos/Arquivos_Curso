# conta quantidade de caracteres 
a = input("Digite um número inteiro para saber a quantidade de digitos: ")
print("A quantidade de digitos é:",len(a))

#inverte a string
while True:
    try:
        i = input("\nDigite uma quantidade de números inteiros que deseja ver invertida: ")
        if len(i) < 100 and i.isdigit():
            numero_invertido = i[::-1]
            print("O número invertido é:", numero_invertido)
            break
        else:
            print("Por favor, digite um número válido com menos de 100 dígitos.")
    except ValueError:
             print("Por favor, digite apenas números para o RG.")

#inverte a string de modo mais simples
i=input("\nDigite um número inteiro para ser invertido: ")
string_invertida = i[::-1]
print("O número invertido é:",string_invertida)


def data(data):
    if data [3:5]=="01":
        print(f"\n{data[0:2]} de janeiro de {data[6:]}")

data("01/01/2024")


import random

def embaralhar_palavra(palavra):
    letras_embaralhadas = random.sample(palavra, len(palavra))
    palavra_embaralhada = ''.join(letras_embaralhadas)
    return palavra_embaralhada
po = input ("\nDigite a palavra que deseja embaralhar: ")
pe = embaralhar_palavra(po)
print(f"Palavra original: {po}")
print(f"Palavra embaralhada: {pe}")


import math 
def calc():
  
    opm = input("\nBem vindo a Calculadora Python:\n(1) Multiplicação\n(2) Divisão\n(3) Adição\n(4) Subtração\nDigite a operação desejada: ")
    n1=int(input("\nDigite o primeiro número para realizar a operação desejada: "))
    n2=int(input("Digite o segundo número para realizar a operação desejada: "))
    if opm == "1":
        mult=n1*n2
        print("O resultado da operação é:",mult)

    elif opm == "2":
        div=n1/n2
        print("O resultado da operação é:",div)

    elif opm == "3":
        adi=n1+n2
        print("O resultado da operação é:",adi)

    elif opm == "4":
        sub=n1-n2
        print("O resultado da operação é:",sub)

calc()