# lojas tabajara
while True:
    inicio = int(input("1 - Para iniciar\n0 - Para sair\n"))
    if inicio==0:
        print('Compra finalizada')
        break
    if inicio ==1:
        prod=1
        soma=0
        while (prod!=0):
            prod=float(input("Digite o valor do produto: R$ "))
            soma=soma+prod
            print("O total a pagar é: R$",soma)
            break
    vp=float(input("Digite o valor pago em dinheiro pelo Cliente: R$ "))
    troco = (vp-soma)
    print("O troco será do cliente será de: R$",troco,"\n")