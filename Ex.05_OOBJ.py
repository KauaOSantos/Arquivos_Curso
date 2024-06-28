def valor_pagamento ():
    cont=0
    total=0
    while True:
        valor_prestacao = float(input("\nDigite o Valor da Prestação:R$ "))
        print(valor_prestacao)
        dias_de_atraso = int(input("Digite os dias de atraso: "))
        print(dias_de_atraso)

        juros=(valor_prestacao*0.1/100)*dias_de_atraso
        
        print("O valor de juros é: R$",juros)
        print("O valor da prestação com os juros é: R$",valor_prestacao+juros)
        print("O valor da prestação com a multa é: R$",valor_prestacao+valor_prestacao*0.03)
        cont=cont+1
        total=total+(valor_prestacao+valor_prestacao*0.03)
        
        inicio = int(input("\nDigite 1 para continuar ou 0 para encerrar: "))
        if inicio == 1:
            print("programa reiniciado")
        elif inicio == 0:
            print("Programa encerrado")
            break
        else:
            print("Valor inválido digite 1 ou 0 !!!")

        
    print("\n O total de compras foi:",cont)
    print(" O total de vendas foi: R$",total)

valor_pagamento()