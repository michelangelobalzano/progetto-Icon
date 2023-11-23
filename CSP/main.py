from hill_climbing import hill_climbing, valutazione
from preprocessing import preprocessing
from prettytable import PrettyTable

lista_giocatori = preprocessing()

print("Calcolo migliore formazione\n")

# Scelta del modulo
print("Moduli disponibili: 433, 442, 4231, 352")
while True:
    scelta = int(input("Inserire modulo: "))

    if(scelta == 433 or scelta == 4231 or scelta == 442 or scelta == 352):
        break
    else:
        print("Modulo non valido!")
if scelta == 433:
    modulo = ['Portiere', 'Terzino sinistro', 'Difensore centrale', 'Difensore centrale', 'Terzino destro', 'Centrocampista centrale', 'Mediano', 'Centrocampista centrale', 'Ala sinistra', 'Prima punta', 'Ala destra']
elif scelta == 4231:
    modulo = ['Portiere', 'Terzino sinistro', 'Difensore centrale', 'Difensore centrale', 'Terzino destro', 'Mediano', 'Mediano', 'Ala sinistra', 'Trequartista', 'Ala destra', 'Prima punta']
elif scelta == 442:
    modulo = ['Portiere', 'Terzino sinistro', 'Difensore centrale', 'Difensore centrale', 'Terzino destro', 'Esterno sinistro', 'Centrocampista centrale', 'Centrocampista centrale', 'Esterno destro', 'Prima punta', 'Prima punta']
elif scelta == 352:
    modulo = ['Portiere', 'Difensore centrale', 'Difensore centrale', 'Difensore centrale', 'Esterno sinistro', 'Centrocampista centrale', 'Mediano', 'Centrocampista centrale', 'Esterno destro', 'Prima punta', 'Prima punta']

# Scelta del budget
print("Budget minimo: 300 (milioni)")
print("Budget massimo: 500 (milioni)")
while True:
    budget = int(input("Inserire budget: "))

    if(budget >= 300 and budget <= 500):
        break
    else:
        print("Budget non valido")

# Calcolo della formazione
formazione = hill_climbing(modulo, lista_giocatori, budget)
costo, overall = valutazione(formazione)

# Creazione di una tabella per la stampa della formazione
tabella_formazione = PrettyTable(["Nome", "Overall", "Posizione", "Costo (milioni di euro)"])

for giocatore in formazione:
    tabella_formazione.add_row(giocatore)

tabella_formazione.add_row(["", "", "", ""])
tabella_formazione.add_row(["TOTALE", overall, "", costo])

# Stampa della tabella
print(tabella_formazione)