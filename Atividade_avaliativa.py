class Cadastro_Pc:
    def __init__(self, nome, senha, matricula, fone, email, endereco):
        self.nome = nome
        self.__senha = senha
        self.matricula = matricula
        self.__fone = fone
        self.__email = email
        self.__endereco = endereco


class Cadastro_BO:
    def __init__(self, tipo, vitima, acusado, tel_vitima, email_vitima, endereco_vitima):
        self.tipo = tipo
        self.__vitima = vitima
        self.acusado = acusado
        self.__tel_vitima = tel_vitima
        self.__email_vitima = email_vitima
        self.__endereco_vitima = endereco_vitima


class Cadastro_preso:
    def __init__(self, nome, acusacao, dn, sexo, endereco, condenacao):
        self.nome = nome
        self.acusacao = acusacao
        self.dn = dn
        self.sexo = sexo
        self.endereco = endereco
        self.condenacao = condenacao


class PC:
    def __init__(self):
        self.cadastros = [] 

    def cadastro_pc(self):
        nome = input("Digite seu nome para cadastrar: ")
        senha = input("Digite uma senha: ")
        matricula = input("Digite sua matrícula: ")
        fone = int(input("Digite seu telefone: "))
        email = input("Digite seu email: ")
        endereco = input("Digite seu endereço: ")
        cadastro_pc = Cadastro_Pc (nome, senha, matricula, fone, email, endereco)
       
        self.cadastros.append(cadastro_pc)
        print(f"Policial {nome} cadastrado com sucesso!")

    def cadastro_BO(self):
        tipo = input("Digite o tipo de BO que deseja registrar: ")
        vitima = input("Digite quem é a vítima: ")
        acusado = input("Digite quem é o acusado: ")
        tel_vitima = int(input("Digite o telefone da vítima: "))
        email_vitima = input("Digite o email da vítima: ")
        endereço_vitima = input("Digite o endereço da vítima: ")
        
        cadastro_bo = Cadastro_BO(tipo, vitima, acusado, tel_vitima, email_vitima, endereço_vitima)
        self.bo.append(cadastro_bo)
        print("Boletim de Ocorrência cadastrado com sucesso!")

    def cadastro_preso(self):
        nome = input("Digite o nome do preso: ")
        acusacao = input("Digite a acusação dele: ")
        dn = input("Digite a data de nascimento dele: ")
        sexo = input("Digite o sexo do preso: ")
        endereco = input("Digite seu endereço: ")
        condenacao = input("Digite a condenação do preso: ")

        cadastro_pc = Cadastro_Pc (nome, acusacao, dn, sexo, endereco, condenacao)
        self.pc.append(cadastro_pc)
        print("Preso cadastrado com sucesso!")

    def relatorio(self): # dando erro nessa parte
        print("\nRelatório:")
        for Cadastro_Pc in self.relatorio:
            print("Policiais:",Cadastro_Pc,"\nCadastros de BO:",Cadastro_BO," Presos:",Cadastro_preso)


    def menu(self):
        while True:
            print("\n1 - Relatório\n2 - Cadastrar Policial\n3 - Cadastrar BO\n4 - Cadastrar preso\n5 - Finalizar ")
            try:
                opcao = int(input("Escolha a opção que deseja: "))
                if opcao == 1:
                    self.relatorio()
                elif opcao == 2:
                    self.cadastro_pc()
                elif opcao == 3:
                    self.cadastro_BO()
                elif opcao == 4:
                    self.cadastro_preso()
                elif opcao == 5:
                    print("Programa encerrado")
                    break
                else:
                    print("Opção inválida! Digite um número de 1 a 5.")
            except ValueError:
                print("Erro: Digite um número válido para a opção.")