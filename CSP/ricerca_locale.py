import random

# Scelta di un calciatore casuale per posizione
def calciatore_casuale(posizione, lista_calciatori):
    while True:
        calciatore = random.choice(lista_calciatori)
        if (calciatore[2] == posizione):
            break
    return calciatore

# Funzione che restituisce il costo totale e l'overall medio di una formazione
def punteggi(formazione):
    costo = 0
    overall = 0
    for c in formazione:
        costo = costo + c[3]
        overall = overall + c[1]
    overall = overall / 11
    return costo, round(overall, 2)

# Metodo di inizializzazione
def random_restart(modulo, lista_calciatori, budget):
    while True:
        formazione = []
        for p in modulo:
            while True:
                calciatore = calciatore_casuale(p, lista_calciatori)
                if (calciatore not in formazione):
                    break
            formazione.append(calciatore)
        costo, _ = punteggi(formazione)
        if (costo < budget):
            break
    return formazione