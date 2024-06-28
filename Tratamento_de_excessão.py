# utilizado para tratar a mensagem de erro 
try:
    a=int(input("Digite um número: "))
except ValueError: 
    print(" Digite apenas números ")
except:
    print("Erro desconhecido")
else:
    print("Deu certo")
finally:
    print("fim do algoritmo")  