from ricerca_locale import *
import matplotlib.pyplot as plt

######################################################################################################################
TASSO_PEGGIORAMENTO = 1.03 # Percentuale di peggioramento consentito

######################################################################################################################
# Metodo per la creazione del grafico del test dell'algoritmo
def grafico(risultati, lista):
    plt.plot(lista, risultati, marker='o')
    plt.xlabel('Numero massimo di iterazioni')
    plt.ylabel('Overall medio ottenuto')
    plt.title('Algoritmo Hill Climbing')
    plt.grid(True)
    plt.savefig("CSP/grafici/hc.png")
    plt.show()

######################################################################################################################
# Metodo per il test dell'algoritmo
def test_hc(modulo, lista_calciatori, budget, numero_test):
    lista_max_iterazioni = [20, 50, 100, 200, 500] # Lista max iterazioni da testare
    risultati = [] # Risultati ottenuti per ogni valore di max iterazioni

    # Test per ogni valore di max iterazioni
    for m in lista_max_iterazioni:

        # Risultati dei singoli test sul valore max iterazioni
        somma = 0

        # Effettuazione del singolo test
        for _ in range(numero_test):
            formazione = hill_climbing(modulo, lista_calciatori, budget, m)
            _, overall = punteggi(formazione)
            somma = somma + overall

        # Inserimento del risultato ottenuto con il valore di max iterazioni
        media = round(somma / numero_test, 2)
        risultati.append(media)

    grafico(risultati, lista_max_iterazioni)

######################################################################################################################
# Metodo per ottenere i risultati per il confronto degli algoritmi
def risultati_hc(modulo, lista_calciatori, budget, numero_test):
    max_iterazioni = 500
    risultati = []
    # Effettuazione del singolo test
    for _ in range(numero_test):
        formazione = hill_climbing(modulo, lista_calciatori, budget, max_iterazioni)
        _, overall = punteggi(formazione)
        risultati.append(overall)
    return risultati

######################################################################################################################
# Funzione di valutazione
def valutazione(c1, c2, o1, o2, oc1, oc2, budget):
    return ((c2 < budget) and (o1 < o2) or ((c2 < c1) and (oc1 <= oc2 * TASSO_PEGGIORAMENTO)))

######################################################################################################################
# Hill Climbing
def hill_climbing(modulo, lista_calciatori, budget, max_iterazioni):
    
    # Random restart
    formazione = random_restart(modulo, lista_calciatori, budget)
    iterazioni = 0

    # Walk
    while True:
        costo, overall = punteggi(formazione)

        # Per ogni posizione si prova ad effettuare una sostituzione
        for i, posizione in enumerate(modulo):

            # Pesca casuale del calciatore
            while True:
                nuovo_calciatore = calciatore_casuale(posizione, lista_calciatori)
                if (nuovo_calciatore not in formazione):
                    break

            # Creazione nuova formazione
            formazione_temp = formazione.copy()
            formazione_temp[i] = nuovo_calciatore

            # Valutazione nuova formazione
            costo_nuovo, overall_nuovo = punteggi(formazione_temp)
            if (valutazione(costo, costo_nuovo, overall, overall_nuovo, formazione[i][1], formazione_temp[i][1], budget)):
                formazione = formazione_temp
                costo = costo_nuovo
                overall = overall_nuovo
                
        iterazioni = iterazioni + 1
        if iterazioni == max_iterazioni:
            break

    return formazione