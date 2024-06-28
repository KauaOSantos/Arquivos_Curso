
from matplotlib import pyplot as plt 

x_dias=[1,5,10,15,20,25,30]
y_temp_max=[28,27,29,30,32,26,24]
y_temp_min=[18,17,19,22,24,20,13]

plt.plot(x_dias,y_temp_max)


import emoji 
resposta = input ("Você está feliz ou triste? (F/T): ")
if resposta.upper() == 'F':
    print(emoji.emojize("Fico feliz por você :grinning_face_with_big_eyes: "))
elif resposta.upper() == 'T': 
    print(emoji.emojize("Espero que se sinta melhor em breve! :pensive_face: "))
else: 
    print("Resposta Inválida.")