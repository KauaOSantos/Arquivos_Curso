a="EDERSON"
# função para contar e mostrar a quantidade de letras ou números dentro dos parenteses: print(len(variavel))
a="Ederson"
print(len(a))

# função para deixar a primeira letra da variável maiúscula: print(variável.capitalize())
print(a.capitalize())

# função para deixar toda variável maiúscula: print(a.upper())
print(a.upper())

# função para deixar toda variável minúscula: print(a.casefold())
print(a.casefold())

# Função que responde True ou False para ver se a variável é toda minúscula: print(a.islower())
print(a.islower())

# Função que responde True ou False para ver se a variável é toda maiúscula: print(a.isupper())
print(a.isupper())

# função que responde True ou False para verificar se a string possui só números: print(variável.isdigit())
a="12345"
print(a.isdigit())
b="12345abc"
print(b.isdigit())

# método para trocar todas as ocorrências de uma substring por outra em uma string: print(variável.replace("substring","que vai substituir"))
c="Ederson Roberto" 
print(c.replace("Roberto","Costa"))

a="Ederson-Roberto-Costa"
print(a.split("-"))
# método que retorna onde a substring começa na string:
a="Ederson Roberto Costa"
print(a.find("Costa"))
# operador "in" verifica se uma substring é parte de uma string com True ou False 
a="Ederson Roberto Costa"
print("dias"in a)
#operador "count" retorna a frequência de ocorrência do parâmetro passado: print(a.count("a"))
print(a.count("a"))

# a função: print(s[])
s="Olá, mundo!" 
print(s[0])
print(s[2])
print(s[6])
print(s[0:3]) 
print(s[0:3])
print(s[0:3])