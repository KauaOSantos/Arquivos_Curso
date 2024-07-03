from Conta import *



while True:
    try:
        menu = int(input("\n    Menu de serviços  \n0 - Sair\n1 - Cadastro\n2 - Saldo\n3 - Saque\n4 - Depósito\n"))
        
        if menu == 1:   
            x=Conta()     
            
        elif menu == 2:
            x.extrato()
            
        elif menu == 3:  
            x.saque()

        elif menu == 4: 
            x.deposito()    
        
        elif menu == 0:
            break
            
        else:
            print("Opção inválida")
    except ValueError:
        print("Inválido")
        continue