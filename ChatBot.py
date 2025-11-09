import openai


openai.api_key = "api_ia" 

def enviar_missatge_ia(missatge):

    try:
        resposta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Ets amable i util"},
                {"role": "user", "content": missatge}
            ]
        )
        return resposta.choices[0].message.content.strip()
    except Exception as e:
        return "No s'ha pogut contactar amb la IA. Revisa la teva connexió o la clau d'API."


def main():
    print("=== XATBOT IA ===")
    print("Escriu 'sortir' per acabar la conversa.\n")

    while True:
        usuari = input("Tu: ")

        if usuari.lower() == "sortir":
            print("IA: Adeu!")
            break

        resposta = enviar_missatge_ia(usuari)
        print("IA:", resposta)


if __name__ == "__main__":
    main()
