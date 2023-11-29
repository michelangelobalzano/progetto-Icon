import pandas as pd

######################################################################################################################
# Dizionario per sostituzioni delle sigle delle posizioni
mappa_posizioni = {'GK': 'Portiere', 'RB': 'Terzino destro', 'CB': 'Difensore centrale',
                    'LB': 'Terzino sinistro', 'CM': 'Centrocampista centrale', 'CDM': 'Mediano',
                    'CAM': 'Trequartista', 'RW': 'Ala destra', 'ST': 'Prima punta', 'LW': 'Ala sinistra',
                    'LM': 'Esterno sinistro', 'RM': 'Esterno destro'}

######################################################################################################################
# Metodo che crea il dataset adatto per il CSP
def creazione_dataset():

    # Caricamento dataset
    dataset = pd.read_csv('dataset/dataset.csv')
    # Colonne da mantenere
    colonne = ['Known As', 'Overall', 'Positions Played', 'Value(in Euro)']
    # Selezione delle colonne
    ds = dataset[colonne]
    # Conversione da euro in milioni di euro del valore
    ds.loc[:, 'Value(in Euro)'] = ds['Value(in Euro)'] / 1000000
    # Salvataggio dataset
    ds.to_csv("dataset\dataset_CSP.csv", index = False)

######################################################################################################################
# Preprocessing del dataset per la creazione del vettore dei calciatori
def preprocessing():

    # Creazione del dataset da effettuare in caso di modifica del dataset
    # creazione_dataset()

    # Caricamento del dataset
    dataset = pd.read_csv('dataset/dataset_CSP.csv')

    lista_calciatori = []
    for index, row in dataset.iterrows():
        # Creazione di una tupla per ogni posizione di ogni singolo calciatore
        posizioni = [pos.strip() for pos in row['Positions Played'].split(',')]

        # Creazione di una tupla per ogni posizione del calciatore
        for posizione in posizioni:
            # Sostituzione sigla posizione con nome posizione
            nome_posizione = mappa_posizioni.get(posizione, posizione)
            calciatore = (row['Known As'], row['Overall'], nome_posizione, row['Value(in Euro)'])

            # Inserimento calciatore nel vettore
            lista_calciatori.append(calciatore)
    return lista_calciatori