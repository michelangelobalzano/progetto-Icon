from main_manager import *
import random
from ricerca_locale import *
from preprocessing import preprocessing


DIMENSIONE_POPOLAZIONE = 50
NUMERO_GENERAZIONI = 1

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
    # Punto di taglio per il crossover
    crossover_point = random.randint(1, len(parent1) - 1)

    # Geni prima del punto di taglio presi da parent1, dopo da parent2
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    # Geni prima del punto di taglio presi da parent2, dopo da parent1
    child2 = parent2[:crossover_point] + parent1[crossover_point:]

    return child1, child2

######################################################################################################################
# Mutazione (scambio casuale di due calciatori)
def mutate(individuo):
    # Scegli due posizioni diverse nel modulo
    posizione1, posizione2 = random.sample(modulo, 2)

    # Trova gli indici delle posizioni nel modulo
    index1 = modulo.index(posizione1)
    index2 = modulo.index(posizione2)

    # Scambia i due calciatori alle posizioni scelte
    individuo_mutato = list(individuo)
    individuo_mutato[index1], individuo_mutato[index2] = individuo_mutato[index2], individuo_mutato[index1]

    return tuple(individuo_mutato)

######################################################################################################################
# Algoritmo Genetico
def genetic_algorithm(modulo, lista_calciatori, budget):
    popolazione = [random_restart(modulo, lista_calciatori, budget) for _ in range(DIMENSIONE_POPOLAZIONE)]

    for generazione in range(NUMERO_GENERAZIONI):
        # Creazione vettore contenente la valutazione per ogni individuo
        valutazioni = [fitness(individuo, budget) for individuo in popolazione]

        # Selezione degli individui più adatti
        genitori = [popolazione[i] for i in range(DIMENSIONE_POPOLAZIONE) if valutazioni[i] > 0]

        # Creazione di una nuova generazione attraverso crossover e mutazione
        nuova_generazione = []

        while len(nuova_generazione) < DIMENSIONE_POPOLAZIONE:
            genitore1, genitore2 = roulette_wheel_selection(popolazione, valutazioni)
            figlio1, figlio2 = crossover(genitore1, genitore2)
            #figlio = mutate(figlio)
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
budget = 500

miglior_formazione = genetic_algorithm(modulo, lista_calciatori, budget)
stampa(miglior_formazione)