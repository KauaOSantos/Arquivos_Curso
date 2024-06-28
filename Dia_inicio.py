
 #1 Pergunta e resposta ao usuário, #2 Preenchimento com a e b,
 #3 Quantidade de vezes quer que repita um texto, #4 Formando um Quadrado 

 #1 Pergunta e resposta ao usuário 
idade=int(input("Digite a idade: "))
print(type(idade))
salario=int(input("Digite o salário: "))
imposto=float(input("Digite o imposto: "))

sal=int(input('Digite o salario:'))
print ("O salário digitado foi %d"%sal)
 
 #2 Preenchimento com a e b 
a="Kauã"
b="Miguel"
print("Prezado "+a+" "+b+" . "+"Olá!")
print("Prezado",a,b,".","Olá!")
print("Prezado %s %s. Olá!"%(a,b))

 #3 Quantas vezes quer que repita um texto
print(10*"Senac Hub Academy\n")

 #4 Formando um quadrado
print("+"+10*"-"+"+")
print(("|"+" "*10 +"|\n")*5, end="")
print("+"+10*"-"+"+")
nome=input('Nome: ')
sal=float(input('Salário: '))
print('O funcionário %s recebeu R$ %.2f'%(nome,sal))


frase ='Um triângulo de base igual a {0} e altura igual a {1} possui área igual a {2}.'.format(3,4,12)
print (frase) 