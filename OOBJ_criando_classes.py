'''class Sample: # a class sempre deve iniciar maiúscula
    def __init(self,a,b):
        self.a = a
        self.b = b
    def func(self):
        print(self.a, self.b)    
'''
class Vendedor():
    def __init__(self,nome,vendas):
        self.nome = nome
        self.vendas = vendas

# vendedor1=Vendedor('Kauã', 5000)
# print(vendedor1.nome)
# print(vendedor1.vendas)

    def vendeu (self,vendas):
        self.vendas = vendas 
        print(self.vendas)
    def bateu_meta(self,meta):
        if self.vendas>meta:
            print("Bateu Meta")
        else:
            print("Não Bateu a meta")
# vendedor2 = Vendedor("Ederson",1000)
# print(vendedor2.nome)
# vendedor2.bateu_meta(100)