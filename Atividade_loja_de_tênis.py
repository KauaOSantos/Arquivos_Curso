class Produto:
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

class LojaTenis:
    def __init__(self):
        self.produtos = [] 

    def cadastrar_produto(self):
        codigo = input("Digite o código do produto: ")
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        produto = Produto(codigo, nome, preco)
        self.produtos.append(produto)
        print(f"Produto {nome} cadastrado com sucesso!")

    def alterar_produto(self):
        codigo = input("Digite o código do produto que deseja alterar: ")
        produto_encontrado = False
        for produto in self.produtos:
            if produto.codigo == codigo:
                novo_nome = input("Digite o novo nome do produto: ")
                novo_preco = float(input("Digite o novo preço do produto: R$ "))
                produto.nome = novo_nome
                produto.preco = novo_preco
                print(f"Produto {codigo} alterado com sucesso!")
                produto_encontrado = True
                break
        
        if not produto_encontrado:
            print("Produto não encontrado!")

    def relatorio_produtos(self):
        print("\nRelatório de Produtos:")
        for produto in self.produtos:
            print(f"Código: {produto.codigo}, Nome: {produto.nome}, Preço: R${produto.preco}")

    def menu(self):
        while True:
            print("\n1 - Cadastro\n2 - Alterar cadastro\n3 - Relatório de cadastro\n4 - Sair")
            try:
                opcao = int(input("Escolha uma opção: "))
                if opcao == 1:
                    self.cadastrar_produto()
                elif opcao == 2:
                    self.alterar_produto()
                elif opcao == 3:
                    self.relatorio_produtos()
                elif opcao == 4:
                    print("Programa encerrado")
                    break
                else:
                    print("Opção inválida! Digite um número de 1 a 4.")
            except ValueError:
                print("Erro: Digite um número válido para a opção.")