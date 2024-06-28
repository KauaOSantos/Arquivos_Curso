# soma dos elementos 
t=[[1,2], [3], [4,5,6]]
soma = sum(t[0] + t[1] + t[2])
print(soma)
# outras maneira
print(t[0][0]+t[0][1]+t[1][0]+t[2][0]+t[2][1]+t[2][2])
print(t[0][1]*t[1][0]-t[2][2])

i=[1, 2, 3]
print ([i[0], i[0]+i[1], i[0]+i[1]+i[2]])

# deletar as duas extremidades do elemento
j=[1,2,3,4]
del j[0]
del j[-1]
print(j)

# adicionar elementos na lista
country=["Alemanha", "Itália", "Japão"]
country.insert(1,"Brasil")
print (country) 

country=["Alemanha", "Itália", "Japão"]
country.insert(2,"Brasil")
print (country) 

country=["Alemanha", "Itália", "Japão"]
country.insert(5,"Brasil")
print (country) 

#ordem reversa
lista=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista.reverse()
print(lista)