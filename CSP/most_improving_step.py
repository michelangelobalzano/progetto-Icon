from ricerca_locale import *
import matplotlib.pyplot as plt

######################################################################################################################
# Percentuale di peggioramento consentito
TASSO_PEGGIORAMENTO = 1.03

######################################################################################################################
# Metodo per il test dell'algoritmo
def test_mis(modulo, lista_calciatori, budget, numero_test):
    lista_max_iterazioni = [20, 50, 100, 200, 500] # Lista max iterazioni da testare
    risultati = [] # Risultati ottenuti per ogni valore di max iterazioni

    # Test per ogni valore di max iterazioni
    for m in lista_max_iterazioni:

        # Risultati dei singoli test sul valore max iterazioni
        somma = 0

        # Effettuazione del singolo test
        for _ in range(numero_test):
            formazione = most_improving_step(modulo, lista_calciatori, budget, m)
            _, overall = punteggi(formazione)
            somma = somma + overall

        # Inserimento del risultato ottenuto con il valore di max iterazioni
        media = round(somma / numero_test, 2)
        risultati.append(media)

    grafico(risultati, lista_max_iterazioni)


######################################################################################################################
# Metodo per ottenere i risultati per il confronto degli algoritmi
def risultati_mis(modulo, lista_calciatori, budget, numero_test):
    max_iterazioni = 500
    risultati = []
    # Effettuazione del singolo test
    for _ in range(numero_test):
        formazione = most_improving_step(modulo, lista_calciatori, budget, max_iterazioni)
        _, overall = punteggi(formazione)
        risultati.append(overall)
    return risultati


######################################################################################################################
# Funzione di valutazione
def valutazione(c1, c2, o1, o2, oc1, oc2, budget):
    return ((c2 < budget) and (o1 < o2) or ((c2 < c1) and (oc1 <= oc2 * TASSO_PEGGIORAMENTO)))

######################################################################################################################
# Most Improving Step
def most_improving_step(modulo, lista_calciatori, budget, max_iterazioni):
    
    # Random restart
    formazione = random_restart(modulo, lista_calciatori, budget)
    iterazioni = 0
    
    # Walk
    while iterazioni < max_iterazioni:

        # Calcolo dei punteggi attuali
        costo_migliore, overall_migliore = punteggi(formazione)

        # Creazione di 11 possibili sostituzioni
        formazione2 = random_restart(modulo, lista_calciatori, budget)

        posizione_migliore = None
        calciatore_migliore = None

        # Ricerca della migliore mossa
        for i, c in enumerate(formazione2):            
            
            # Controllo che il giocatore non sia già presente nella formazione iniziale
            if c not in formazione:
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
                
        # Effettuazione della sostituzione migliore
        if posizione_migliore is not None: 
            formazione[posizione_migliore] = calciatore_migliore
        
        iterazioni = iterazioni + 1

    return formazione

######################################################################################################################
# Metodo per la creazione del grafico del test dell'algoritmo
def grafico(risultati, lista):
    plt.plot(lista, risultati, marker='o')
    plt.xlabel('Numero massimo di iterazioni')
    plt.ylabel('Overall medio ottenuto')
    plt.title('Algoritmo Most Improving Step')
    plt.grid(True)
    plt.savefig("CSP/grafici/mis.png")
    plt.show()

        