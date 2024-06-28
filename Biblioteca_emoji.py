import emoji

resposta = input("Você está feliz ou triste? (F/T): ")

if resposta.upper() == 'F':
    print(emoji.emojize("Fico feliz por você :grinning_face_with_big_eyes: "))
elif resposta.upper() == 'T': 
    print(emoji.emojize("Espero que se sinta melhor em breve! :pensive_face: "))
else: 
    print("Resposta Inválida.")