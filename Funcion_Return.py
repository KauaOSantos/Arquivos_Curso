def cadastro():
    name=input("Qual é o seu nome: ")
    age= int(input("Qual sua idade: ")) 
    return name,age

print("Iniciando cadastro...")
nome,idade=cadastro()
print("Cadastro realizado com sucesso: ")
print("Seu nome é",nome,"e você tem",idade,"anos de idade")