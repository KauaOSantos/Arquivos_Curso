class Conta():
    def __init__(self):
        self.nome = input("\nDigite o seu nome: ")
        self.__saldo=0
        self.__cpf = input("\nDigite o seu CPF: ")
        self.__senha = int(input("\nDigite a sua senha: "))
        

    def extrato(self):
        senha = int(input("\nPara ver o seu extrato, digite a senha: "))
        if (senha == self.__senha):
            print("R$",self.__saldo)
            
        else:
            print("Senha Inválida.")
            

    def deposito(self):
        valor = float(input("\nDigite o valor que deseja depositar em sua conta: "))
        self.__saldo+=valor
        print(f"O valor depositado foi: R${valor}")
        

    # def saque(self):
    #     while True:
    #         __senha = input("\nDigite o valor que deseja sacar: ")
    #         if (saque <=__saldo): 
    #             print("R$",__saldo)
    #         else:
    #             print("Saldo inválido.")