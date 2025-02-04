import random
import json
import datetime


def carica_highscore():
    try:
        with open("highscore.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def salva_highscore(highscore):
    with open("highscore.json", "w") as file:
        json.dump(highscore, file, indent=4)


def indovina_il_numero():
    numero_da_indovinare = random.randint(1, 100)
    tentativi = 0
    inizio_tempo = datetime.datetime.now()

    print("Benvenuto nel game! Indovina il numero tra 1 e 100.")

    while True:
        try:
            tentativo = input("? ")
            if not tentativo.isdigit():
                raise ValueError("Input errato. Riprova.")

            tentativo = int(tentativo)
            tentativi += 1

            if tentativo < numero_da_indovinare:
                print("Troppo basso")
            elif tentativo > numero_da_indovinare:
                print("Troppo alto")
            else:
                tempo_fine = datetime.datetime.now()
                durata = (tempo_fine - inizio_tempo).total_seconds()
                print(f"Hai indovinato in {tentativi} tentativi! 🎉 Tempo impiegato: {durata:.2f} secondi.")
                return tentativi, durata
        except ValueError:
            print("Inserisci un numero intero.")


def aggiorna_highscore(tentativi, durata):
    nome = input("Inserisci il tuo nome: ")
    data_e_ora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    nuovo_record = {"nome": nome, "tentativi": tentativi, "data_e_ora": data_e_ora, "durata": durata}

    highscore = carica_highscore()
    highscore.append(nuovo_record)
    highscore = sorted(highscore, key=lambda x: x["tentativi"])

    salva_highscore(highscore)


def visualizza_highscore():
    highscore = carica_highscore()
    if not highscore:
        print("Nessun highscore registrato.")
        return

    print("Highscore:")
    for record in highscore:
        print(
            f"{record['nome']}: - Tentativi: {record['tentativi']} - Data: {record['data_e_ora']} - Tempo: {record['durata']:.2f} sec")


def chiedi_continuare():
    risposta = input("\nVuoi continuare a giocare? (s/n): ").strip().lower()
    return risposta in ["s", "si"]

if __name__ == "__main__":
    while True:
        tentativi, durata = indovina_il_numero()
        aggiorna_highscore(tentativi, durata)
        visualizza_highscore()

        if not chiedi_continuare():
            print("Grazie per aver partecipato!")
            break
