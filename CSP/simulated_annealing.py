import math
import random
from ricerca_locale import *
import matplotlib.pyplot as plt

######################################################################################################################
# Temperatura iniziale da raffreddare
TEMPERATURA_INIZIALE = 2000

######################################################################################################################
# Metodo per la creazione del grafico del test dell'algoritmo
def grafico(risultati, lista):
    plt.plot(lista, risultati, marker='o')
    plt.xlabel('Tasso di raffreddamento')
    plt.ylabel('Overall medio ottenuto')
    plt.title('Algoritmo Simulated Annealing')
    plt.grid(True)
    plt.savefig("CSP/grafici/sa.png")
    plt.show()
    
######################################################################################################################
# Metodo per il test dell'algoritmo
def test_sa(modulo, lista_calciatori, budget, numero_test):
    lista_tassi_raffreddamento = [0.02, 0.015, 0.01, 0.005, 0.002] # Lista tassi di raffreddamento da testare
    risultati = [] # Risultati ottenuti per ogni valore di tassi di raffreddamento

    # Test per ogni valore di tassi di raffreddamento
    for tr in lista_tassi_raffreddamento:

        # Risultati dei singoli test sul valore tassi di raffreddamento
        somma = 0

        # Effettuazione del singolo test
        for _ in range(numero_test):
            formazione = simulated_annealing(modulo, lista_calciatori, budget, tr)
            _, overall = punteggi(formazione)
            somma = somma + overall

        # Inserimento del risultato ottenuto con il valore di tassi di raffreddamento
        media = round(somma / numero_test, 2)
        risultati.append(media)

    grafico(risultati, lista_tassi_raffreddamento)

######################################################################################################################
# Metodo per ottenere i risultati per il confronto degli algoritmi
def risultati_sa(modulo, lista_calciatori, budget, numero_test):
    tasso_raffreddamento = 0.002
    risultati = []
    # Effettuazione del singolo test
    for _ in range(numero_test):
        formazione = simulated_annealing(modulo, lista_calciatori, budget, tasso_raffreddamento)
        _, overall = punteggi(formazione)
        risultati.append(overall)
    return risultati

######################################################################################################################
# Funzione di valutazione
def valutazione(c1, c2, o1, o2, budget, temperatura):

    # Calcolo probabilità di accettazione di una sostituzione peggiorativa
    # Normalizzazione dei valori usando la funzione tanh
    normalized_cost_difference = math.tanh((c2 - c1) / temperatura)

    # Calcolo della probabilità di accettare la soluzione peggiorativa usando la funzione tanh
    probabilita = (1 + normalized_cost_difference) / 2
    
    return (c2 < budget and (o2 >= o1 or random.random() < probabilita))

######################################################################################################################
# Simulated Annealing
def simulated_annealing(modulo, lista_calciatori, budget, tasso_raffreddamento):

    # Random restart
    formazione = random_restart(modulo, lista_calciatori, budget)
    costo, overall = punteggi(formazione)

    # Inizializzazione temperatura
    temperatura = TEMPERATURA_INIZIALE

    # Walk
    while temperatura > 0.1:
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

            if (valutazione(costo, costo_nuovo, overall, overall_nuovo, budget, temperatura)):
                formazione = formazione_temp
                costo = costo_nuovo
                overall = overall_nuovo

            # Abbassamento della temperatura
            temperatura *= 1 - tasso_raffreddamento
    return formazione