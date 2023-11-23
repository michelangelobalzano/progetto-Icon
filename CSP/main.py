from hill_climbing import *
from simulated_annealing import *
from tabu_search import *
from preprocessing import preprocessing
from input_manager import *

NUMERO_TEST = 50

lista_calciatori = preprocessing()

print("CALCOLO MIGLIORE FORMAZIONE\n")

# Scelta del modulo e budget
modulo = input_modulo()
budget = input_budget()

# Hill Climbing
test_hc(modulo, lista_calciatori, budget, NUMERO_TEST)
# Tabu Search
test_ts(modulo, lista_calciatori, budget, NUMERO_TEST)
# Simulated Annealing
test_sa(modulo, lista_calciatori, budget, NUMERO_TEST)