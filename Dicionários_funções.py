
tradutor = {}
tradutor ["pineapple"] = "abacaxi"
tradutor ["apple"] = "maça"
tradutor ["orange"] = "laranja"
print(type(tradutor))
print(tradutor)

cor = {}
cor ["Yellow"] = "amarelo"
cor ["green"] = "verde"
cor ["red"] = "vermelho"
print(type(cor))
print(cor)

tradutor1 = {}
tradutor1 = {"pineapple":"abacaxi","apple":"maça","orange":"laranja"}
print(tradutor1)

# deletar elemento do dicionário
tradutor1 = {}
tradutor1 = {"pineapple":"abacaxi","apple":"maça","orange":"laranja"}
print(tradutor1)
del(tradutor1["apple"])
print(tradutor1)

# vê se a fruta está na lista e mostra a mensagem
print(tradutor1.pop('banana','Fruta não encontrada'))
# remove todos os elementos do dicionário
tradutor1.clear()
print(tradutor1)

# boleano que vê se tem o elemento no dicionário
tradutor1 = {}
tradutor1 = {"pineapple":"abacaxi","apple":"maça","orange":"laranja"}
print("pineapple" in tradutor1)

dados = {
    'crossfox': {'km': 35000, 'ano': 2005},
    'DSS': {'km': 17000, 'ano': 2015},
    'passat': {'km': 35000, 'ano': 2005}
}

print(dados['DSS']['ano'])  # Acessando o ano do carro 'DSS'