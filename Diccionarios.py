meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "una respuesta a una broma",
            "SHEESH": "ligera desaprobación",
            "CREEPY": "aterrador, siniestro",
            "AGGRO": "ponerse agresivo/enojado"
            }
for i in range(5):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

    if word in meme_dict.keys():
        print(word, "significa:", meme_dict [word])
        # ¿Qué debemos hacer si se encuentra la palabra?
    else:
        print("Esa palabra no está escrita en el diccionario")
            
