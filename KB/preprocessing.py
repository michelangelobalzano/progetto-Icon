from pyswip import Prolog
from unidecode import unidecode
import re
import pandas as pd 

# normalizzazione delle parole
def normalizzazione(parola):
    # trasformare tutte le lettere in minuscolo
    parola = parola.lower()
    # togliere i puntini che abbreviano i nomi
    parola = parola.replace(".", "")
    # togliere gli apostrofi dai cognomi
    parola = parola.replace("'", "")
    # togliere gli spazi
    parola = parola.replace(" ", "_")
    # togliere i trattini dai cognomi
    parola = parola.replace("-", "_")
    # togliere tutti gli accenti dalle lettere
    parola = unidecode(parola)

    return parola

# caricamento del dataset
df = pd.read_csv("dataset/dataset.csv", nrows=500)

# selezione delle colonne utili
dataset = df[["Known As", "Overall", "Nationality", "Club Name","Club Jersey Number","Best Position"]]

# creazione delle clausole dei calciatori
with open("prolog_files/kb_calciatori_query.pl", "w") as file_prolog:
    for index, row in dataset.iterrows():
        # recupero dei dati dalla singola tupla
        nome = row["Known As"]
        overall = row["Overall"]
        nazionalita = row["Nationality"]
        squadra = row["Club Name"]
        numero_maglia = row["Club Jersey Number"]
        ruolo = row["Best Position"]  # Utilizza espressione regolare per separare i ruoli
        
        # normalizzazione delle stringhe
        nome = normalizzazione(nome)
        squadra = normalizzazione(squadra)
        nazionalita = normalizzazione(nazionalita)
        ruolo = normalizzazione(ruolo)
        
        # creazione della clausola
        clausola = f"calciatore('{nome}', {overall}, '{nazionalita}', '{squadra}', {numero_maglia}, '{ruolo}')."
        
        # scrittura della clausola
        file_prolog.write(clausola + "\n")