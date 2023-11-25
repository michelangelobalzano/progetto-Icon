from main_manager import *
import random
import math
from ricerca_locale import *
from preprocessing import preprocessing
import numpy as np



#################
# DA FARE
# - controllare che non ci siano duplicati nei figli creati con il crossover
# - controllare le condizioni sugli overall e sui costi come per la mutazione nel crossover
# - se uno dei due controll fallisce si ripete con un altro tentativo
#################

'''
CODICE DI CHAT GPT:
#####################################################################
def are_players_unique(child):
    seen_players = set()
    for player in child:
        if player in seen_players:
            return False
        seen_players.add(player)
    return True

def crossover(parent1, parent2):
    max_prove = 5
    prove = 0
    effettuato = False

    while prove < max_prove:
        # Punto di taglio per il crossover
        crossover_point = random.randint(1, len(parent1) - 1)

        # Geni prima del punto di taglio presi da parent1, dopo da parent2
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        # Geni prima del punto di taglio presi da parent2, dopo da parent1
        child2 = parent2[:crossover_point] + parent1[crossover_point:]

        costo1, _ = punteggi(child1)
        costo2, _ = punteggi(child2)

        if costo1 <= budget and costo2 <= budget and are_players_unique(child1) and are_players_unique(child2):
            effettuato = True
            break

        prove += 1

    if effettuato:
        return child1, child2
    else:
        return parent1, parent2
#########################################################################
'''










######################################################################################################################
# Percentuale di peggioramento consentito
TASSO_PEGGIORAMENTO = 0.03
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
# Crossover (a un punto)
def crossover(parent1, parent2):
    max_prove = 5
    prove = 0
    effettuato = False

    while (prove < max_prove):
        # Punto di taglio per il crossover
        crossover_point = random.randint(1, len(parent1) - 1)

        # Geni prima del punto di taglio presi da parent1, dopo da parent2
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        # Geni prima del punto di taglio presi da parent2, dopo da parent1
        child2 = parent2[:crossover_point] + parent1[crossover_point:]

        costo1, _ = punteggi(child1)
        costo2, _ = punteggi(child2)
        if (costo1 <= budget and costo2 <= budget):
            effettuato = True
            break
        prove = prove + 1
    if (effettuato):
        return child1, child2
    else:
        return parent1, parent2

######################################################################################################################
# Mutazione (scambio casuale di due calciatori)
def mutate(individuo, lista_calciatori):
    max_prove = 5
    prove = 0

    indice = min(enumerate(individuo), key=lambda x: x[1][1])[0]
    calciatore_selezionato = individuo[indice]

    individuo_mutato = list(individuo)
    while (prove < max_prove):
        # Pesca casuale del calciatore
        nuovo_calciatore = calciatore_casuale(calciatore_selezionato[2], lista_calciatori)

        if (nuovo_calciatore not in individuo):
            # Sostituzione del calciatore
            individuo_mutato[indice] = nuovo_calciatore
            c1, o1 = punteggi(individuo)
            c2, o2 = punteggi(individuo_mutato)
            if ((c2 < budget) and (o1 < o2) or ((c2 < c1) and (individuo[indice][1] <= individuo_mutato[indice][1] * TASSO_PEGGIORAMENTO))):
                break
            else:
                individuo_mutato[indice] = calciatore_selezionato
        prove = prove + 1

    return tuple(individuo_mutato)

######################################################################################################################
# Algoritmo Genetico
def genetic_algorithm(modulo, lista_calciatori, budget):
    popolazione = [random_restart(modulo, lista_calciatori, budget) for _ in range(DIMENSIONE_POPOLAZIONE)]

    for i in popolazione:
        _, overall = punteggi(i)

    for generazione in range(NUMERO_GENERAZIONI):
        # Creazione vettore contenente la valutazione per ogni individuo
        valutazioni = [fitness(individuo, budget) for individuo in popolazione]

        # Selezione degli individui più adatti
        genitori = [popolazione[i] for i in range(DIMENSIONE_POPOLAZIONE) if valutazioni[i] > 0]

        # Creazione di una nuova generazione attraverso crossover e mutazione
        nuova_generazione = []

        while len(nuova_generazione) < DIMENSIONE_POPOLAZIONE:
            genitore1, genitore2 = roulette_wheel_selection(popolazione, valutazioni)
            '''print("Genitore 1: ", genitore1)
            print("\n\nGenitore 2: ", genitore2)'''

            figlio1, figlio2 = crossover(genitore1, genitore2)

            '''print("\n\nFiglio 1: ", figlio1)
            print("\n\nFiglio 2: ", figlio2)'''

            figlio1 = mutate(figlio1, lista_calciatori)
            figlio2 = mutate(figlio2, lista_calciatori)

            '''print("\n\nFiglio 1 mutato: ", figlio1)
            print("\n\nFiglio 2 mutato: ", figlio2)'''

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