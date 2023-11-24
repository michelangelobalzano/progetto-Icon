from hill_climbing import *
from simulated_annealing import *
from tabu_search import *
from most_improving_step import *
from preprocessing import preprocessing
from input_manager import *
import os
from prettytable import PrettyTable
from ricerca_locale import punteggi

MAX_ITERAZIONI = 500
TASSO_RAFFREDDAMENTO = 0.002

def clearConsole():
    command = "clear"
    if os.name in ("nt", "dos"):  # If Machine is running on Windows, use cls
        command = "cls"
    os.system(command)

def stampa(formazione):
    tabella = PrettyTable(["Nome", "Overall", "Posizione", "Costo"])
    for calciatore in formazione:
        tabella.add_row(calciatore)
    tabella.add_row(["", "", "", ""])
    costo, overall = punteggi(formazione)
    tabella.add_row(["TOTALE", overall, "", costo])
    print(tabella)

# Test degli algoritmi singolarmente
def test_algoritmi():
    modulo = ['Portiere', 'Terzino sinistro', 'Difensore centrale', 'Difensore centrale', 
              'Terzino destro', 'Centrocampista centrale', 'Mediano', 'Centrocampista centrale', 
              'Ala sinistra', 'Prima punta', 'Ala destra']
    budget = 400
    numero_test = 50

    # Recupero lista dei calciatori
    lista_calciatori = preprocessing()

    clearConsole()
    print("SCEGLIERE ALGORITMO\n")
    print("1 = Hill Climbing")
    print("2 = Tabu Search")
    print("3 = Simulated Annealing")
    print("4 = Most Improving Step")
    while True:
        scelta = int(input("Inserire scelta: "))
        if(scelta >= 1 and scelta <= 4):
            break
        else:
            print("Scelta non valida!")

    if (scelta == 1):
        test_hc(modulo, lista_calciatori, budget, numero_test)
    elif (scelta == 2):
        test_ts(modulo, lista_calciatori, budget, numero_test)
    elif (scelta == 3):
        test_sa(modulo, lista_calciatori, budget, numero_test)
    elif (scelta == 4):
        test_mis(modulo, lista_calciatori, budget, numero_test)




# Confronto tra tutti gli algoritmi
def confronto_algoritmi():
    modulo = ['Portiere', 'Terzino sinistro', 'Difensore centrale', 'Difensore centrale', 
              'Terzino destro', 'Centrocampista centrale', 'Mediano', 'Centrocampista centrale', 
              'Ala sinistra', 'Prima punta', 'Ala destra']
    budget = 400
    numero_test = 50

    # Recupero lista dei calciatori
    lista_calciatori = preprocessing()

    # Recupero vettore dei risultati da ogni algoritmo
    ris_hc = risultati_hc(modulo, lista_calciatori, budget, numero_test)
    ris_ts = risultati_ts(modulo, lista_calciatori, budget, numero_test)
    ris_sa = risultati_sa(modulo, lista_calciatori, budget, numero_test)
    ris_mis = risultati_mis(modulo, lista_calciatori, budget, numero_test)

    # Creazione grafico confronto
    plt.boxplot([ris_hc, ris_ts, ris_sa, ris_mis], 
                labels=['HC', 'TS', 'SA', 'MIS'])
    plt.ylabel('Valutazione')
    plt.title('Confronto risultati degli algoritmo')
    plt.savefig("CSP/grafici/confronto.png")
    plt.show()



def calcolo_singolo():
    clearConsole()
    print("SCEGLIERE ALGORITMO\n")
    print("1 = Hill Climbing")
    print("2 = Tabu Search")
    print("3 = Simulated Annealing")
    print("4 = Most Improving Step")
    while True:
        scelta = int(input("Inserire scelta: "))
        if(scelta >= 1 and scelta <= 4):
            break
        else:
            print("Scelta non valida!")
    
    clearConsole()
    # Recupero lista dei calciatori
    lista_calciatori = preprocessing()
    # Input modulo e budget
    modulo = input_modulo()
    budget = input_budget()

    if (scelta == 1):
        formazione = hill_climbing(modulo, lista_calciatori, budget, MAX_ITERAZIONI)
    elif (scelta == 2):
        formazione = tabu_search(modulo, lista_calciatori, budget, MAX_ITERAZIONI)
    elif (scelta == 3):
        formazione = simulated_annealing(modulo, lista_calciatori, budget, TASSO_RAFFREDDAMENTO)
    elif (scelta == 4):
        formazione = most_improving_step(modulo, lista_calciatori, budget, MAX_ITERAZIONI)

    stampa(formazione)