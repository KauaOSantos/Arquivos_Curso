while True:
    usuário=(input("Digite seu nome de usuário: "))
    senha=(input( "Digite a senha: "))
    if usuário == senha:
        print('Erro, digite outra senha !!')
    else:
        print("Acesso liberado")