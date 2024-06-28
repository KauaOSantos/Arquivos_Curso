while True:
    valor = int(input("\nDigite o valor 1 ou 0 para encerrar: "))
    if valor == 1:
        continue
    elif valor == 0:
        print("Programa encerrado")
        break
    else:
        print("Valor inválido. Digite 1 ou 0 !!!")

# Inicializa o contador
num = 100

# Loop enquanto o contador for maior que 0
while num > 0:
    # Verifica se o número é igual a 5
    if num == 5:
        # Se for 5, apenas decrementa sem imprimir e continua para o próximo número
        num -= 1
        continue
    
    # Imprime o número atual
    print(num)
    
    # Decrementa o número para continuar a contagem regressiva
    num -= 1
    
num = 100
while num < 100:
    num - 1
    if num == 5:
        continue
    print(num)