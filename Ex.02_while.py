while True:
    opm=(input(" Calculadora:\n Se deseja parar digite: (0)\n Para Multiplicação digite: (1)\n para Divisão digite: (2)\n Para Adição digite: (3)\n Para Subtração digite: (4)\n"))
    if opm == "0":
        print('Fim')
        break
    n1=float(input("Digite o primeiro número para realizar a operação desejada: "))
    n2=float(input("Digite o segundo número para realizar a operação desejada: "))


    if opm == "1":
        mult=n1*n2
        print(mult)

    elif opm == "2":
        div=n1/n2
        print(div)

    elif opm == "3":
        adi=n1+n2
        print(adi)

    elif opm == "4":
        sub=n1-n2
        print(sub)