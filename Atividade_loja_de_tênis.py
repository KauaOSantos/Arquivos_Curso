class LojaTenis:
    def __init__(self, cadastro, alteracao, relatorio, sair):
        self.cadastro=cadastro
        self.alteracao=alteracao
        self.relatorio=relatorio
        self.sair=sair
    
def menu():   
    print("\n1 - Cadastro\n2 - Alterar cadastro\n3 - Relatório de cadastro\n4 - Sair")
        

def escolher_opcao():
    while True:
        escolha = input("\nEscolha uma opção: ")
        if len(escolha) == 1 and escolha.isdigit(): # Verifica se a escolha tem dígito numérico
            return int(escolha)
        else:
            print("Por favor, digite uma opção válida com 1 dígito.")


def nome():
    while True:
        nome = input("Digite seu nome: ").title().strip() 
        if nome.replace(" ", "").isalpha():
            LojaTenis
            break
        else:
            print("Por favor, digite apenas letras.")


def cpf():
    while True:
        try:
            cpf = input("Digite seu CPF (11 digitos): ")
            if len(cpf) == 11 and cpf.isdigit(): 
               cpf in LojaTenis
               break
            else:
                print("Por favor, digite um CPF válido com 11 dígitos numéricos.")
        except ValueError:
            print("Por favor, digite apenas números para o CPF.")


def tel():       
    while True:
        try:
            tel = input("Digite seu telefone (11 dígitos): ")
            if len(tel) == 11 and tel.isdigit():  
                tel in LojaTenis
                break
            else:
                print("Por favor, digite um número de telefone válido com 11 dígitos numéricos.")
        except ValueError:
            print("Por favor, digite apenas números para o telefone.")

def alterar():
    opcao = input("Digite o CPF do cliente a ser alterado: ")
    for cpf in LojaTenis:
        if cpf.get('cpf') == cpf:  
            print("O que você deseja alterar?")
            print("1 - Nome")
            print("2 - CPF")
            print("3 - Telefone")

        elif opcao == '1':
            nome()
            ['nome'] = cad_pessoal['nome'] 

        else:
            print("Opção inválida.")
            print("Cliente alterado com sucesso.")
'''
        elif opcao == '1':
            tel()
            pessoa['Nome'] = cad_pessoal['telefone']  # Atualiza o telefone do cliente encontrada
        elif opcao == '5':
            email()
            pessoa['email'] = cad_pessoal['email']  # Atualiza o email do cliente encontrada
        else:
            print("Opção inválida.")
        print("Cliente alterado com sucesso.")

def relatorio(self):
        print(f" Nome:{self.nome} \n Cpf: {self.cpf}\n Telefone: {self.telefone}")'''
    # cadastro = input("")
    #     def alterar(self,botao):
    #     if botao=="+":
    #         print("Aumentar canal")
    #     elif botao=="-":
    #         print("Diminuir canal")
    #     else: 
    #         print("Valor Inválido")