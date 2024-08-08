cad_completo = []  # Lista para armazenar todos os cadastros completos
cad_pessoal = {}   # Dicionário para armazenar informações pessoais de um cadastro

def menu():    #Exibe o menu de serviços disponíveis
    print("\n    Menu de serviços    \n1 - Cadastro\n2 - Excluir Cadastro\n3 - Alterar cadastro\n4 - Listar Clientes\n5 - Relatório de serviço\n6 - Sair")

def escolher_opcao():    #Solicita ao usuário que escolha uma opção
    while True:
        escolha = input("\nEscolha uma opção: ")
        if len(escolha) == 1 and escolha.isdigit(): # Verifica se a escolha tem dígito numérico
            return int(escolha)
        else:
            print("Por favor, digite uma opção válida com 1 dígito.")

def cadastrar():    # Realiza o cadastro de uma nova pessoa
    nome()
    cpf()
    rg()
    tel()
    email()
    veiculo()
    cad_completo.append(cad_pessoal.copy()) # Adiciona uma cópia das informações pessoais à lista de cadastros completos
    cad_pessoal.clear()  # Limpa o dicionário para o próximo cadastro

def nome(): #Solicita e valida o nome do cliente
    while True:
        nome = input("Digite seu nome: ").title().strip()  #  e remoção de espaços em branco
        if nome.replace(" ", "").isalpha():  # Verifica se o nome contém apenas letras após a remoção de espaços
            cad_pessoal['nome'] = nome  # Armazena o nome no dicionário cad_pessoal
            break
        else:
            print("Por favor, digite apenas letras.")

def cpf():   #Solicita e valida o RG do cliente
    while True:
        try:
            cpf = input("Digite seu CPF (11 digitos): ")
            if len(cpf) == 11 and cpf.isdigit():  # Verifica se o CPF tem 11 dígitos numéricos
                cad_pessoal['cpf'] = cpf  # Armazena o CPF no dicionário cad_pessoal
                break
            else:
                print("Por favor, digite um CPF válido com 11 dígitos numéricos.")
        except ValueError:
            print("Por favor, digite apenas números para o CPF.")

def rg():     #Solicita e valida o RG do cliente
    while True:
        try:
            rg = input("Digite seu RG (7 digitos): ")
            if len(rg) == 7 and rg.isdigit():  # Verifica se o RG tem 7 dígitos numéricos
                cad_pessoal['rg'] = rg  # Armazena o RG no dicionário cad_pessoal
                break
            else:
                print("Por favor, digite um RG válido com 7 dígitos numéricos.")
        except ValueError:
            print("Por favor, digite apenas números para o RG.")

def tel():       #Solicita e valida o telefone do cliente

    while True:
        try:
            tel = input("Digite seu telefone (11 dígitos): ")
            if len(tel) == 11 and tel.isdigit():  # Verifica se o telefone tem 11 dígitos numéricos
                cad_pessoal['telefone'] = tel  # Armazena o telefone no dicionário cad_pessoal
                break
            else:
                print("Por favor, digite um número de telefone válido com 11 dígitos numéricos.")
        except ValueError:
            print("Por favor, digite apenas números para o telefone.")

def email():    #Solicita e valida o email do cliente

    while True:
        email = input("Digite seu email: ").strip()  # Remove espaços em branco no início e fim
        if email:  # Verifica se o email não está vazio
            cad_pessoal['email'] = email  # Armazena o email no dicionário cad_pessoal
            break
        else:
            print("O campo de email não pode ficar em branco. Por favor, digite seu email.")

def veiculo():    #Solicita e valida as informações do veículo
    try:
        marca = input("Digite a marca do veículo: ")
        if not marca.isalpha(): # Verifica se a variável 'marca' não contém apenas letras.
            raise ValueError("Digite apenas letras.")
        
        modelo = input("Digite o modelo do veículo: ")
        if not modelo.isalpha(): # Verifica se a variável 'marca' não contém apenas letras.
            raise ValueError("Digite apenas letras.")
        
        placa = input("Digite a placa do veículo: ")
        if not placa.isalnum(): # Verifica se a variável 'placa' não contém apenas letras e números.
            raise ValueError("Digite apenas letras e números.")
        
        ano_de_fabricacao = int(input("Digite o ano de fabricação do veículo: "))
        if not isinstance(ano_de_fabricacao, int):
            raise ValueError("Digite apenas números.")
        
        problema = input("Digite o problema do veículo: ")
        if not problema.replace(" ", "").isalpha():  # Permite espaços no problema
            raise ValueError("Digite apenas letras.")
        
        # Retorna um dicionário com as informações do veículo
        return {
            'marca': marca,
            'modelo': modelo,
            'placa': placa,
            'ano_de_fabricacao': ano_de_fabricacao,
            'problema': problema
        }
        
    except ValueError as ve:
        print(f"Erro: {ve}")
        return None  # Retorna None se houver erro nas entradas
    
def deletar():  #Exclui o cadastro de um cliente da lista cad_completo com base no CPF
    cpf = input("Digite o CPF do cliente a ser deletado: ")
    for pessoa in cad_completo:
        if pessoa.get('cpf') == cpf:  # Verifica se encontrou o CPF na lista de cadastros completos
            cad_completo.remove(pessoa)  # Remove a pessoa da lista
            print(f"Cliente com CPF {cpf} foi deletado.")
            return
    print(f"Cliente com CPF {cpf} não encontrado.")

def alterar(): #Altera informações de cadastro de um cliente na lista cad_completo com base no CPF
    cpf = input("Digite o CPF do cliente a ser alterado: ")
    for pessoa in cad_completo:
        if pessoa.get('cpf') == cpf:  # Verifica se encontrou o CPF na lista de cadastros completos
            print("O que você deseja alterar?")
            print("1 - Nome")
            print("2 - CPF")
            print("3 - RG")
            print("4 - Telefone")
            print("5 - Email")
            opcao = input("Escolha uma opção: ")
            if opcao == '1':
                nome()
                pessoa['nome'] = cad_pessoal['nome']  # Atualiza o nome do cliente encontrado
            elif opcao == '2':
                cpf()
                pessoa['cpf'] = cad_pessoal['cpf']  # Atualiza o CPF do cliente encontrada
            elif opcao == '3':
                rg()
                pessoa['rg'] = cad_pessoal['rg']  # Atualiza o RG do cliente encontrada
            elif opcao == '4':
                tel()
                pessoa['telefone'] = cad_pessoal['telefone']  # Atualiza o telefone do cliente encontrada
            elif opcao == '5':
                email()
                pessoa['email'] = cad_pessoal['email']  # Atualiza o email do cliente encontrada
            else:
                print("Opção inválida.")
            print("Cliente alterado com sucesso.")
            return
    print(f"Cliente com CPF {cpf} não encontrado.")

def listar_clientes():    #Lista todos os clientes cadastrados na lista cad_completo
    print("\nLista de Clientes:")
    for idx, pessoa in enumerate(cad_completo, 1):
        print(f"\nCliente {idx}:")
        print(f"Nome: {pessoa['nome']}")
        print(f"CPF: {pessoa['cpf']}")
        print(f"RG: {pessoa['rg']}")
        print(f"Telefone: {pessoa['telefone']}")
        print(f"Email: {pessoa['email']}")

    for x,veiculo in cad_completo:
        # if 'veiculo' in pessoa:  # Verifica se há informações de veículo cadastradas
        print("Veículo:")
        print(f"Marca: {pessoa['veiculo']['marca']}")
        print(f"Modelo: {pessoa['veiculo']['modelo']}")
        print(f"Placa: {pessoa['veiculo']['placa']}")
        print(f"Ano de Fabricação: {pessoa['veiculo']['ano_de_fabricacao']}")
        print(f"Problema: {pessoa['veiculo']['problema']}")

def relatorio_servico():    #Exibe um relatório simples sobre os serviços
    print("\nRelatório de Serviço:")
    print(f"Total de clientes cadastrados: {len(cad_completo)}")

def main():    #Função principal que controla o fluxo do programa
    menu()  # Exibe o menu inicial
    while True:
        opcao = escolher_opcao()  # Obtém a opção escolhida pelo usuário
        if opcao == 1:
            cadastrar()  # Chama a função de cadastro
        elif opcao == 2:
            deletar()  # Chama a função de exclusão de cadastro
        elif opcao == 3:
            alterar()  # Chama a função de alteração de cadastro
        elif opcao == 4:
            listar_clientes()  # Chama a função de listagem de clientes
        elif opcao == 5:
            relatorio_servico()  # Chama a função de relatório de serviço
        elif opcao == 6:
            print("Saindo do programa...")
            break  # Encerra o loop e finaliza o programa
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")