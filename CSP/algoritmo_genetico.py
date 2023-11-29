from main_manager import *
import random
import math
from ricerca_locale import *
from preprocessing import preprocessing
import numpy as np

######################################################################################################################
# Percentuale di peggioramento consentito
TASSO_PEGGIORAMENTO = 1.03
DIMENSIONE_POPOLAZIONE = 50
NUMERO_GENERAZIONI = 500

######################################################################################################################
# Funzione di fitness che associa un punteggio a una formazione
def fitness(individuo, budget):
    costo, overall = punteggi(individuo)
    if costo <= budget:
        return overall
    else:
        return 0
    
######################################################################################################################
# Funzione di selezione dei genitori per il crossover in base ad una probabilità dipendente dal fitness
def roulette_wheel_selection(popolazione, valutazioni):
    somma_fitness = sum(valutazioni)
    probabilita_selezione = [fitness / somma_fitness for fitness in valutazioni]

    # Selezione casuale in base alle probabilità
    genitore1 = random.choices(popolazione, weights=probabilita_selezione)[0]
    genitore2 = random.choices(popolazione, weights=probabilita_selezione)[0]

    return genitore1, genitore2

######################################################################################################################
# Funzione di controllo duplicati nei figli del crossover
def senza_duplicati(individuo):
    calciatori_visti = set()
    for c in individuo:
        if c in calciatori_visti:
            return False
        calciatori_visti.add(c)
    return True

######################################################################################################################
# Crossover (a un punto)
def crossover(genitore1, genitore2):

    max_prove = 5
    prove = 0
    effettuato = False

    while (prove < max_prove):
        # Punto di taglio per il crossover
        crossover_point = random.randint(1, len(genitore1) - 1)

        # Creazione dei due figli in base al punto di tagli del crossover
        figlio1 = genitore1[:crossover_point] + genitore2[crossover_point:]
        figlio2 = genitore2[:crossover_point] + genitore1[crossover_point:]

        # Calcolo punteggi genitori
        _, op1 = punteggi(genitore1)
        _, op2 = punteggi(genitore2)

        # Calcolo punteggi figli
        _, o1 = punteggi(figlio1)
        _, o2 = punteggi(figlio2)
        
        # Controllo figli creati
        if (senza_duplicati(figlio1) and senza_duplicati(figlio2)):
            effettuato = True
            break

        prove = prove + 1
    if (effettuato):
        return figlio1, figlio2
    else:
        return genitore1, genitore2

######################################################################################################################
# Mutazione (scambio casuale di due calciatori)
def mutate(individuo, lista_calciatori):
    
    max_prove = 5
    prove = 0

    # Selezione del calciatore con overall minore per la sostituzione
    indice = min(enumerate(individuo), key=lambda x: x[1][1])[0]
    calciatore_selezionato = individuo[indice]

    individuo_mutato = list(individuo)

    while (prove < max_prove):
    
        # Pesca casuale del calciatore
        nuovo_calciatore = calciatore_casuale(calciatore_selezionato[2], lista_calciatori)

        # Test del nuovo calciatore
        if (nuovo_calciatore not in individuo):
            individuo_mutato[indice] = nuovo_calciatore
            c1, o1 = punteggi(individuo)
            c2, o2 = punteggi(individuo_mutato)
            if ((o1 < o2) or ((c2 < c1) and (individuo[indice][1] <= individuo_mutato[indice][1] * TASSO_PEGGIORAMENTO))):
                break
            else:
                individuo_mutato[indice] = calciatore_selezionato
        prove = prove + 1

    return tuple(individuo_mutato)

######################################################################################################################
# Algoritmo Genetico
def genetic_algorithm(modulo, lista_calciatori, budget):

    # Creazione della popolazione
    popolazione = [random_restart(modulo, lista_calciatori, budget) for _ in range(DIMENSIONE_POPOLAZIONE)]

    for generazione in range(NUMERO_GENERAZIONI):
        # Creazione vettore contenente la valutazione per ogni individuo
        valutazioni = [fitness(individuo, budget) for individuo in popolazione]

        # Selezione degli individui con fitness > 0 (costo < budget)
        genitori = [popolazione[i] for i in range(DIMENSIONE_POPOLAZIONE) if valutazioni[i] > 0]

        # Creazione di una nuova generazione attraverso crossover e mutazione
        nuova_generazione = []

        while (len(nuova_generazione) < DIMENSIONE_POPOLAZIONE):
            # Selezione di due genitori in base ad una probabilità dipendente dall'overall
            genitore1, genitore2 = roulette_wheel_selection(popolazione, valutazioni)

            # Crossover
            figlio1, figlio2 = crossover(genitore1, genitore2)

            # Mutazione
            figlio1 = mutate(figlio1, lista_calciatori)
            figlio2 = mutate(figlio2, lista_calciatori)

            # Inserimento dei figli nella nuova generazione
            nuova_generazione.append(figlio1)
            nuova_generazione.append(figlio2)

        popolazione = nuova_generazione

    # Restituisci il miglior individuo
    popolazione_ordinata = sorted(popolazione, key=lambda x: fitness(x, budget), reverse=True)
    miglior_individuo = popolazione_ordinata[0] if popolazione_ordinata else ()
    return miglior_individuo

# Esempio di utilizzo
modulo = ['Portiere', 'Terzino sinistro', 'Difensore centrale', 'Difensore centrale', 
        'Terzino destro', 'Centrocampista centrale', 'Mediano', 'Centrocampista centrale', 
        'Ala sinistra', 'Prima punta', 'Ala destra']
lista_calciatori = preprocessing()
budget = 350

miglior_formazione = genetic_algorithm(modulo, lista_calciatori, budget)
stampa(miglior_formazione)