'''# ex.01 - calculo da área e perímetro de um círculo
class Circulo:

    def __init__(self, raio):
        self.raio = raio
    
    def calculo_area(self):
        area = 3.14159 * (self.raio ** 2)  
        return area
    
    def calculo_perimetro(self):
        perimetro = 2 * 3.14159 * self.raio  
        return perimetro

raio = float(input("Digite o raio do círculo: "))
circulo = Circulo(raio)
area = circulo.calculo_area()
perimetro = circulo.calculo_perimetro()
print(f"A área do círculo com raio {raio} é {area:.2f}")
print(f"O perímetro do círculo com raio {raio} é {perimetro:.2f}")

# ex.02 - calculo da área e perímetro de um triângulo 
class Retangulo:

    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def calculo_area(self):
        area = self.largura * self.altura
        return area
    
    def calculo_perimetro(self):
        perimetro = 2 * (self.largura + self.altura)
        return perimetro

largura = float(input("\nDigite a largura do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))
retangulo = Retangulo(largura, altura)
area = retangulo.calculo_area()
perimetro = retangulo.calculo_perimetro()
print(f"A área do retângulo com largura {largura} e altura {altura} é {area:.2f}")
print(f"O perímetro do retângulo com largura {largura} e altura {altura} é {perimetro:.2f}")

# ex.03 verificação de aprovação com Classes
class Aluno:

    def __init__(self, nome, matricula, notas):
        self.nome = nome
        self.matricula = matricula
        self.notas = notas
    
    def calcular_media(self):
        media = sum(self.notas) / len(self.notas)
        return media
    
    def verificar_aprovacao(self):
        media = self.calcular_media()
        if media >= 7.0:
            return f'O aluno {self.nome} foi aprovado com média {media:.2f}.'
        elif media < 4.0:
            return f'O aluno {self.nome} foi reprovado com média {media:.2f}.'
        else:
            return f'O aluno {self.nome} ficou de exame com média {media:.2f}.'

nome = input("Digite o nome do aluno: ")
matricula = input("Digite a Matrícula do aluno: ")
notas = []

for i in range(4):
    nota = float(input(f"Digite a Nota {i+1}: "))
    notas.append(nota)
aluno = Aluno(nome, matricula, notas)
resultado = aluno.verificar_aprovacao()
print(resultado)
'''
#ex.04
class Funcionario:
    def __init__(self, nome, salario_bruto, cargo):
        self.nome = nome
        self.salario_bruto = salario_bruto
        self.cargo = cargo
        self.beneficio = 0  # Inicializa o benefício como zero

    def calcular_salario_liquido(self):
        imposto = 0.1  # Exemplo de imposto (10% do salário bruto)
        
        # Cálculo do salário líquido
        salario_liquido = self.salario_bruto - (self.salario_bruto * imposto) + self.beneficio
        
        return salario_liquido
    
    def definir_beneficio(self):
        # Método para definir o benefício, solicitando ao usuário
        self.beneficio = float(input(f"Digite o benefício para o cargo de {self.cargo}: "))

    def imprimir_folha_pagamento(self):
        salario_liquido = self.calcular_salario_liquido()
        
        print(f"Nome: {self.nome}")
        print(f"Cargo: {self.cargo}")
        print(f"Salário Bruto: R${self.salario_bruto:.2f}")
        print(f"Benefício: R${self.beneficio:.2f}")
        print(f"Salário Líquido: R${salario_liquido:.2f}")

# Exemplo de utilização do programa
nome = input("Digite o nome do funcionário: ")
salario = float(input("Digite o salário bruto do funcionário: R$ "))
cargo = input("Digite o cargo do funcionário: ")

funcionario = Funcionario(nome, salario, cargo)
funcionario.definir_beneficio()  # Define o benefício baseado no cargo
funcionario.imprimir_folha_pagamento()