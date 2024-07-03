class Conta():
    def __init__(self, nome, saldo, cpf, senha:int):
        self.nome = nome
        self.__saldo = saldo
        self.__cpf = cpf
        self.__senha = senha

        
    def extrato(self, senha):
        if self.__senha == senha:
            print('Nome = ', self.nome)
            print('CPF = ', self.__cpf)
            print('Saldo = ', self.__saldo)
        else:
            print('senha inválida')

    def depositar(self, valor):
        self.__saldo+=valor

    def sacar(self, senha, valor):
        if senha == self.__senha:
            self.__saldo-=valor            
        else:
            print('senha inválida')