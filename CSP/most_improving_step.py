from ricerca_locale import *
import matplotlib.pyplot as plt
from preprocessing import preprocessing

TASSO_PEGGIORAMENTO = 0.03

def stampa(formazione):
    for c in formazione:
        print(c[0], ": ", c[1])
    q,w = punteggi(formazione)
    print("Costo: ", q, " - overall: ", w)

# Funzione di valutazione
def valutazione(c1, c2, o1, o2, oc1, oc2, budget):
    return ((c2 < budget) and (o1 < o2) or ((c2 < c1) and (oc1 <= oc2 * TASSO_PEGGIORAMENTO)))

def most_improving_step(modulo, lista_calciatori, budget, max_iterazioni):
    
    # Random restart
    formazione = random_restart(modulo, lista_calciatori, budget)
    iterazioni = 0

    stampa(formazione)
    
    # Walk
    while iterazioni < max_iterazioni:

        # Calcolo dei punteggi attuali
        costo_migliore, overall_migliore = punteggi(formazione)

        # Creazione di 11 possibili sostituzioni
        formazione2 = random_restart(modulo, lista_calciatori, budget)

        migliorato = False

        # Ricerca della migliore mossa
        for i, c in enumerate(formazione2):            
            
            # Effettuazione della singola sostituzione sulla formazione iniziale
            formazione_temp = formazione.copy()
            formazione_temp[i] = formazione2[i]

            # Calcolo dei punteggi della nuova formazione
            costo_nuovo, overall_nuovo = punteggi(formazione_temp)

            # Verifica se la formazione è migliore di quella attuale
            if(valutazione(costo_migliore, costo_nuovo, overall_migliore, overall_nuovo, formazione[i][1], c[1], budget)):
                posizione_migliore = i
                calciatore_migliore = c
                costo_migliore = costo_nuovo
                overall_migliore = overall_nuovo
                migliorato = True
                
        if(migliorato): 
            formazione[posizione_migliore] = calciatore_migliore
        iterazioni = iterazioni + 1

    return formazione

modulo = ['Portiere', 'Difensore centrale', 'Difensore centrale', 'Difensore centrale', 'Esterno sinistro', 
          'Centrocampista centrale', 'Mediano', 'Centrocampista centrale', 'Esterno destro', 'Prima punta', 'Prima punta']
budget = 350
lista_calciatori = preprocessing()

formazione = most_improving_step(modulo, lista_calciatori, budget, 200)
stampa(formazione)

        