import pandas as pd
from pyswip import Prolog
from preprocessing import preprocessing

# backtracking
def trova_migliore_formazione(modulo):
    formazione_query = 'formazione({}, Calciatori).'.format(modulo)
    for result in prolog.query(formazione_query):
        migliori_calciatori = result['Calciatori']
        for calciatore in migliori_calciatori:
            print(calciatore)
        return  # Termina la funzione dopo aver trovato la prima soluzione

    print("Nessuna formazione trovata.")


nazionalita = input("Inserire nome dello stato in inglese e con iniziale maiuscola oppure 'All': ")
preprocessing(nazionalita)

prolog = Prolog()
prolog.consult("prolog_files/migliore_formazione.pl")
prolog.consult("prolog_files/kb_{}.pl".format(nazionalita))

# Chiama la funzione per ottenere e stampare la formazione
modulo = input("Inserire modulo (433, 352, 4231, 442): ")
trova_migliore_formazione(modulo)