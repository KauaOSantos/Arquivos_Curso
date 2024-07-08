
lista1 = [10, 20, 30, 40]
lista2 = ["spam", "bungee", "swallow"]
print ("\n",lista1, lista2)

lista01 = ["oi", 2.0, 5, [10, 20]]
# conta quantos elementos tem na lista
print ("\n","A quantidade de elementos na lista é:",len(lista01),"\n")

numeros = [17, 123, 87, 34, 66, 8398, 44]
print(numeros[2])
print(numeros[9-8])
print(numeros[-2])
print(numeros[-1],"\n")

# vê se a fruta está dentro da lista e responde True ou False
frutas = ["maçã", "laranja", "banana", "cereja"]
print("maçã"in frutas)
print("pera"in frutas,"\n")
      
frutas1 = ["maçã", "laranja", "banana", "cereja"]
print([1, 2] + [3, 4])
print(frutas1 +[6, 7, 8, 9])
print([]*4)
print([1, 2, ["Olá", "adeus"]]*2,"\n")

a=[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(max(a))# mostra o maior número da lista
print(min(a))# mostra o menor número da lista
print(sum(a))# mostra a soma dos números na lista

# Substituir um elemento da lista
frut = ["banana", "maçã", "cereja"]
frut[0]="pera"
frut[-1]="laranja"
print(frut)

uma_lista=['a', 'b', 'c', 'd', 'e', 'f']
uma_lista[1:3]='x', 'y'
print(uma_lista)

ul=['a', 'd', 'f']
ul[1:1]= ['b', 'c']
print(ul)
ul[4:4] = ['e']

# Adicionar elemento no final da lista
lista= ['1','3','5']
a=34
lista.append(a)
print(lista)

# Deletar algo da lista
l=['um', 'dois', 'três']
del l[1]
print(l)

# Inverte a ordem da lista
y=[88, 81, 82, 83]
y.reverse()
print(y)

# Ordena os valores da lista 
z=[88, 81, 82, 83]
z.sort()
print(z)

# Comando que ordena os valores de ordem reversa
w=[88, 81, 82, 83]
w. lista.sort()
print(w)

# Conta quantas vezes repete um num
a1=[88, 81, 82, 83, 88, 85, 88, 86]
print (a1)
print (a1.count(88))

# Remove o último elemento da lista
a2=[88, 81, 82, 83, 88, 85, 88, 86]
a2.pop()
print (a2)

# Acrescenta um elemento na posição desejada 
listas = [1,2]
listas.extend([3,4])
print (listas)