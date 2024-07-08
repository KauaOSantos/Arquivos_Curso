class Pessoa:


    def __init__(self, nome, idade, endereco, cidade, estado):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cidade = cidade
        self.estado = estado

    def relatorio(self):
        print("Nome.....!",self.nome)
        print("Idade.....!",self.idade)
        print("Endereço.....!",self.endereco)
        print("Cidade.....!",self.cidade)
        print("Estado.....!",self.estado)


class Aluno(Pessoa):


    def __init__(self, mensalidade, nome, idade, endereco, cidade, estado):
        super().__init__(nome, idade, endereco, cidade, estado)
        self.mensalidade = mensalidade
        print("----------------------------------")
        print("Seja bem vindo querido aluno !!!")
        super().relatorio()
        print("Mensalidade:",self.mensalidade)
        print("----------------------------------")


class Professor(Pessoa):
    def __init__(self, salario, nome, idade, endereco, cidade, estado):
        super().__init__(nome, idade, endereco, cidade, estado)
        self.salario = salario
        print("----------------------------------")
        print("Seja bem vindo querido professor !!!")
        super().relatorio()
        print("Salário...:",self.salario)
        print("----------------------------------")


x = Professor("1,200.00", "Ederson", "22", "Aracaju", "Campo Grande", "MS")
y = Aluno("200.00", "José", "17", "Afonso Pena", "Dourados", "MS")