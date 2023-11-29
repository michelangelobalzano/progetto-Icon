from preprocessing import preprocessing
from input_manager import *
import os # Per metodo ClearConsole()
from ricerca_locale import punteggi
import matplotlib.pyplot as plt
from prettytable import PrettyTable

# Algoritmi
from hill_climbing import hill_climbing, test_hc, risultati_hc
from simulated_annealing import simulated_annealing, test_sa, risultati_sa
from tabu_search import tabu_search, test_ts, risultati_ts
from most_improving_step import most_improving_step, test_mis, risultati_mis
from algoritmo_genetico import algoritmo_genetico, test_ag, risultati_ag

######################################################################################################################
# Valori utilizzati per il test e per il confronto di algoritmi
MODULO = ['Portiere', 'Terzino sinistro', 'Difensore centrale', 'Difensore centrale', 
            'Terzino destro', 'Centrocampista centrale', 'Mediano', 'Centrocampista centrale', 
            'Ala sinistra', 'Prima punta', 'Ala destra']
BUDGET = 350
NUMERO_TEST = 500

######################################################################################################################
# Valori utilizzati per il calcolo di una singola formazione
MAX_ITERAZIONI = 500
TASSO_RAFFREDDAMENTO = 0.005
NUM_GENERAZIONI = 500

######################################################################################################################
# Metodo per la pulizia dello schermo
def clearConsole():

    command = "clear"
    if os.name in ("nt", "dos"):
        command = "cls"
    os.system(command)

######################################################################################################################
# Metodo per la stampa di una singola formazione sottoforma di tabella
def stampa(formazione):

    # Creazione intestazione tabella
    tabella = PrettyTable(["Nome", "Overall", "Posizione", "Costo (milioni)"])
    
    # Inserimento dei calciatori
    for giocatore in formazione:
        tabella.add_row(giocatore)
    
    # Inserimento riga dei punteggi
    tabella.add_row(["", "", "", ""])
    costo, overall = punteggi(formazione)
    tabella.add_row(["TOTALE:", overall, "", costo])
    
    # Stampa
    print(tabella)

######################################################################################################################
# Test degli algoritmi singolarmente
def test_algoritmi():

    # Recupero lista dei calciatori
    lista_calciatori = preprocessing()

    clearConsole()

    # Scelta dell'algoritmo
    print("SCEGLIERE ALGORITMO\n")
    print("1 = Hill Climbing")
    print("2 = Tabu Search")
    print("3 = Simulated Annealing")
    print("4 = Most Improving Step")
    print("5 = Algoritmo genetico")
    while True:
        scelta = int(input("Inserire scelta: "))
        if(scelta >= 1 and scelta <= 5):
            break
        else:
            print("Scelta non valida!")

    # Test dell'algoritmo scelto
    if (scelta == 1):
        test_hc(MODULO, lista_calciatori, BUDGET, NUMERO_TEST)
    elif (scelta == 2):
        test_ts(MODULO, lista_calciatori, BUDGET, NUMERO_TEST)
    elif (scelta == 3):
        test_sa(MODULO, lista_calciatori, BUDGET, NUMERO_TEST)
    elif (scelta == 4):
        test_mis(MODULO, lista_calciatori, BUDGET, NUMERO_TEST)
    elif (scelta == 5):
        test_ag(MODULO, lista_calciatori, BUDGET, NUMERO_TEST)

######################################################################################################################
# Confronto tra tutti gli algoritmi
def confronto_algoritmi():

    # Recupero lista dei calciatori
    lista_calciatori = preprocessing()

    # Recupero vettore dei risultati da ogni algoritmo
    ris_hc = risultati_hc(MODULO, lista_calciatori, BUDGET, NUMERO_TEST)
    ris_ts = risultati_ts(MODULO, lista_calciatori, BUDGET, NUMERO_TEST)
    ris_sa = risultati_sa(MODULO, lista_calciatori, BUDGET, NUMERO_TEST)
    ris_mis = risultati_mis(MODULO, lista_calciatori, BUDGET, NUMERO_TEST)
    ris_ag = risultati_ag(MODULO, lista_calciatori, BUDGET, NUMERO_TEST)

    # Creazione grafico confronto
    plt.boxplot([ris_hc, ris_ts, ris_sa, ris_mis, ris_ag], 
                labels=['HC', 'TS', 'SA', 'MIS', 'AG'])
    plt.ylabel('Valutazione')
    plt.title('Confronto risultati degli algoritmi')
    plt.savefig("CSP/grafici/confronto.png")
    plt.show()

######################################################################################################################
# Calcolo di una singola formazione
def calcolo_singolo():

    clearConsole()
    print("SCEGLIERE ALGORITMO\n")
    print("1 = Hill Climbing")
    print("2 = Tabu Search")
    print("3 = Simulated Annealing")
    print("4 = Most Improving Step")
    print("5 = Algoritmo genetico")
    while True:
        scelta = int(input("Inserire scelta: "))
        if(scelta >= 1 and scelta <= 5):
            break
        else:
            print("Scelta non valida!")
    
    clearConsole()

    # Recupero lista dei calciatori
    lista_calciatori = preprocessing()

    # Input modulo e budget
    modulo = input_modulo()
    budget = input_budget()

    # Ricerca squadra
    if (scelta == 1):
        formazione = hill_climbing(modulo, lista_calciatori, budget, MAX_ITERAZIONI)
    elif (scelta == 2):
        formazione = tabu_search(modulo, lista_calciatori, budget, MAX_ITERAZIONI)
    elif (scelta == 3):
        formazione = simulated_annealing(modulo, lista_calciatori, budget, TASSO_RAFFREDDAMENTO)
    elif (scelta == 4):
        formazione = most_improving_step(modulo, lista_calciatori, budget, MAX_ITERAZIONI)
    elif (scelta == 5):
        formazione = algoritmo_genetico(modulo, lista_calciatori, budget, NUM_GENERAZIONI)

    stampa(formazione)