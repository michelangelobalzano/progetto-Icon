import pandas as pd
from unidecode import unidecode # per togliere tutti gli accenti dalle lettere

def preprocessing(nazionalita):
    # caricamento del dataset dal file csv
    dataset = pd.read_csv('dataset/dataset.csv')

    if (nazionalita != 'All'):
        # rimozione di tutti i giocatori tranne quelli della nazionalita in input
        dataset = dataset[dataset['Nationality'] == nazionalita]

    if (nazionalita == 'All' or len(dataset) > 0):
        # colonne utili da mantenere nel dataset
        colonne = ['Known As', 'Overall', 'Positions Played']

        # rimozione delle colonne inutili
        dataset_troncato = dataset[colonne]

        # mantenere solo i primi 100 calciatori in ordine di overall
        dataset_troncato = dataset_troncato.iloc[:100]

        # esportare il dataset su file
        dataset_troncato.to_csv("dataset\dataset_{}.csv".format(nazionalita), index = False)

        # creare file prolog con i fatti sui giocatori della nazionale
        create_prolog_file(nazionalita)
    
    else:
        print ("nazionalita' non valida!")

def create_prolog_file(nazionalita):
    # caricamento del dataset
    dataset = pd.read_csv('dataset/dataset_{}.csv'.format(nazionalita))

    # trasformare i nomi e i ruoli in minuscolo
    dataset['Known As'] = dataset['Known As'].str.lower()
    dataset['Positions Played'] = dataset['Positions Played'].str.lower()

    # creare vettore per memorizzare le tuple
    prolog_data = []

    # ciclo per recuperare le tuple dal dataset
    for index, row in dataset.iterrows():
        # recupero dati singola tupla
        nome = row['Known As']
        ruoli = row["Positions Played"].split(",")
        overall = row['Overall']

        # togliere i puntini che abbreviano i nomi
        nome = nome.replace(".", "")
        # togliere gli apostrofi dai cognomi
        nome = nome.replace("'", "")
        # togliere gli spazi
        nome = nome.replace(" ", "_")
        # togliere i trattini dai cognomi
        nome = nome.replace("-", "_")
        # togliere tutti gli accenti dalle lettere
        nome = unidecode(nome)

        # inserimento di una tupla per ogni ruolo del singolo giocatore nel vettore
        for ruolo in ruoli:
            prolog_data.append((nome, ruolo, overall))

    # stampare il vettore delle tuple sul file prolog
    with open('prolog_files/kb_{}.pl'.format(nazionalita), 'w') as prolog_file:
        for data in prolog_data:
            prolog_file.write(f'calciatore({data[0]}, {data[1]}, {data[2]}).\n')