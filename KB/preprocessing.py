from unidecode import unidecode
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
dataset = df[["Known As", "Overall", "Potential", "Nationality", "Club Name","Club Jersey Number","Best Position", "Preferred Foot", "Contract Until", "Joined On"]]

# creazione delle clausole dei calciatori
with open("prolog_files/kb_fatti.pl", "w") as file_prolog:
    for index, row in dataset.iterrows():
        # recupero dei dati dalla singola tupla
        nome = row["Known As"]
        overall = row["Overall"]
        potenziale = row["Potential"]
        nazionalita = row["Nationality"]
        squadra = row["Club Name"]
        numero = row["Club Jersey Number"]
        ruolo = row["Best Position"]
        piede = row["Preferred Foot"]
        scadenza = row["Contract Until"]
        inizio = row["Joined On"]
        
        # normalizzazione delle stringhe
        nome = normalizzazione(nome)
        squadra = normalizzazione(squadra)
        nazionalita = normalizzazione(nazionalita)
        ruolo = normalizzazione(ruolo)
        piede = normalizzazione(piede)
        
        # creazione e scrittura delle clausole
        file_prolog.write(f"% Clausole relative a {nome}\n")
        clausola = f"overall('{nome}', {overall})."
        file_prolog.write(clausola + "\n")
        clausola = f"potenziale('{nome}', {potenziale})."
        file_prolog.write(clausola + "\n")
        clausola = f"nazionalita('{nome}', {nazionalita})."
        file_prolog.write(clausola + "\n")
        clausola = f"squadra('{nome}', {squadra})."
        file_prolog.write(clausola + "\n")
        clausola = f"numero('{nome}', {numero})."
        file_prolog.write(clausola + "\n")
        clausola = f"ruolo('{nome}', {ruolo})."
        file_prolog.write(clausola + "\n")
        clausola = f"piede('{nome}', {piede})."
        file_prolog.write(clausola + "\n")
        clausola = f"scadenza('{nome}', {scadenza})."
        file_prolog.write(clausola + "\n")
        clausola = f"inizio('{nome}', {inizio})."
        file_prolog.write(clausola + "\n\n")