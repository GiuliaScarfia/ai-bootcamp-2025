import random

def indovina_il_numero():
    numero_da_indovinare = random.randint(1, 100)
    tentativi = 0

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
                print(f"Hai indovinato in {tentativi} tentativi! 🎉")
                break
        except ValueError:
            print("Inserisci un numero intero.")

if __name__ == "__main__":
    indovina_il_numero()
