while True:
    try:
     cad=int(input("Digite a opção:\n 1 - cadastro\n 0 - sair\n "))
    except:
        print("Número inválido digite 1 ou 0 !!!")
    
    else:
        if (cad == 1):
            nome=(input("Digite o seu nome: "))
            try:
              idade=int(input("Digite a sua idade:"))
            except:
              print("Digite uma idade válida")

            try:
              rg=int(input("Digite o seu RG:"))
            except:
              print("Digite uma RG válido")

        elif (cad==0):   
            print("Programa encerrado") 
            break
        else:
           print("Opção inválida")
