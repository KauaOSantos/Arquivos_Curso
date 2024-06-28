age=int(input("Digite a sua idade para saber se pode dirigir: "))
if(age>17):
    print('Você é maior, já pode dirigir!')
elif(age<18):
     print('Você é menor, não pode dirigir ainda!')

idade=int(input("Digite sua idade: "))
if idade>=16 and idade<18: # caso verdadeiro 
    print ("Pode votar")
elif idade <16:
    print("Apenas estude")
else:
    print("Pode Dirigir")
