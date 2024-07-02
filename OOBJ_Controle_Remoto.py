class ControleRemoto():
    def __init__(self,cor,altura,profundidade,largura):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura
    
    def mudar_canal(self,botao):
        if botao=="+":
            print("Aumentar canal")
        elif botao=="-":
            print("Diminuir canal")
        else: 
            print("Valor Inválido")