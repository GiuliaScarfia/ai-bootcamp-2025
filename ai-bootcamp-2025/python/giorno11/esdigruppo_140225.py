def esdigruppo(sequenza_di_nomi: list):
    if not sequenza_di_nomi:
        return {}

    conteggio_nomi = {}

    for nome in sequenza_di_nomi:
        if nome in conteggio_nomi:
            conteggio_nomi[nome] += 1
        else:
            conteggio_nomi[nome] = 1

    return conteggio_nomi
