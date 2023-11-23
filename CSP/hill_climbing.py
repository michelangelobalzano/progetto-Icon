from preprocessing import pre
import random

# Scelta di un giocatore casuale per posizione
def giocatore_casuale(posizione, lista_giocatori):
    while True:
        giocatore = random.choice(lista_giocatori)
        if (giocatore[2] == posizione):
            break
    return giocatore

# Funzione di valutazione
def valutazione(formazione):
    costo = 0
    overall = 0
    for c in formazione:
        costo = costo + c[3]
        overall = overall + c[1]
    overall = overall / 11
    return costo, round(overall, 2)

# Metodo di inizializzazione
def random_restart(modulo, lista_giocatori, budget):
    while True:
        formazione = []
        for p in modulo:
            while True:
                giocatore = giocatore_casuale(p, lista_giocatori)
                if (giocatore not in formazione):
                    break
            formazione.append(giocatore)
        costo, _ = valutazione(formazione)
        if (costo < budget):
            break
    return formazione

# Metodo di ricerca locale
def hill_climbing(modulo, lista_giocatori, budget):
    # Random restart
    formazione = random_restart(modulo, lista_giocatori, budget)
    max_iterazioni = 0
    # Walk
    while True:
        _, overall_attuale = valutazione(formazione)

        # Per ogni posizione si prova ad effettuare una sostituzione
        for i, posizione in enumerate(modulo):
            # Pesca casuale del giocatore
            while True:
                nuovo_giocatore = giocatore_casuale(posizione, lista_giocatori)
                if (nuovo_giocatore not in formazione):
                    break

            # Creazione nuova formazione
            formazione_temp = formazione.copy()
            formazione_temp[i] = nuovo_giocatore

            # Valutazione nuova formazione
            costo_nuovo, overall_nuovo = valutazione(formazione_temp)
            if costo_nuovo < budget and overall_attuale < overall_nuovo:
                formazione = formazione_temp
                break

        max_iterazioni = max_iterazioni + 1
        if max_iterazioni == 100:
            break
    return formazione