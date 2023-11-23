from pyswip import Prolog

# Inizializza l'interprete Prolog
prolog = Prolog()

# Carica il file Prolog con le clausole nel database
prolog.consult("kb.pl")

# Formula una query
query1 = "numero_disponibile(lazio, 132)"  # Esempio di query

# Stampare i risultati
result = list(prolog.query(query1))

print(bool(result))

query_result = list(prolog.query("miglior_giocatore_squadra_reparto('f_chiesa')"))

print(bool(query_result))
