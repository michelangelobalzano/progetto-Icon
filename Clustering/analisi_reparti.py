import pandas as pd
import matplotlib.pyplot as plt
from preprocessing import preprocessing
from pca import pca

# Mappatura di ogni posizione in un reparto
mappa_posizioni = {'GK': 'Portiere',
                   'CB': 'Difensore',
                   'LB': 'Difensore',
                   'RB': 'Difensore',
                   'LWB': 'Difensore',
                   'RWB': 'Difensore',
                   'CDM': 'Centrocampista',
                   'CM': 'Centrocampista',
                   'LM': 'Centrocampista',
                   'RM': 'Centrocampista',
                   'CAM': 'Centrocampista',
                   'LW': 'Centrocampista',
                   'RW': 'Centrocampista',
                   'CF': 'Attaccante',
                   'ST': 'Attaccante'
}
# Mappatura di un colore per ogni reparto
mappa_colori = {'Portiere': 'skyblue', 
                'Difensore': 'lightcoral', 
                'Centrocampista': 'lightgreen', 
                'Attaccante': 'gold'}

CALCIATORI_PER_CLUSTER = 4 # Numero di calciatori da mostrare per reparto

######################################################################################################################
# Stampa grafico posizioni
def grafico_posizioni(dataset):

    # Conteggio delle posizioni
    conteggio_posizioni = dataset['Best Position'].value_counts()

    # Creazione grafico posizioni
    plt.figure(figsize=(8, 6))
    plt.bar(conteggio_posizioni.index, conteggio_posizioni, color=conteggio_posizioni.index.map(mappa_posizioni).map(mappa_colori))
    plt.title('Conteggio per Posizione')
    plt.xlabel('Posizione')
    plt.ylabel('Conteggio')
    handles = [plt.Rectangle((0, 0), 1, 1, color=mappa_colori[label]) for label in mappa_colori]
    plt.legend(handles, mappa_colori.keys(), title='Reparto', loc='upper right')
    #plt.savefig("Clustering/grafici/posizioni.png")
    plt.show()

######################################################################################################################
# Stampa grafico reparti
def grafico_reparti(dataset):

    # Conteggio dei reparti
    conteggio_reparti = dataset['Reparto'].value_counts()

    # Creazione grafico reparti
    plt.figure(figsize=(8, 6))
    plt.bar(conteggio_reparti.index, conteggio_reparti, color=conteggio_reparti.index.map(mappa_colori))
    plt.title('Conteggio per Reparto')
    plt.xlabel('Reparto')
    plt.ylabel('Conteggio')
    #plt.savefig("Clustering/grafici/reparti.png")
    plt.show()

######################################################################################################################
# Stampa grafico reparti PCA
def grafico_reparti_PCA(dataset):

    reparti = ["Portiere", "Difensore", "Centrocampista", "Attaccante"]
    for reparto in reparti:
        dati_reparto = dataset[dataset['Reparto'] == reparto]
        plt.scatter(dati_reparto['PC1'], dati_reparto['PC2'], c=mappa_colori.get(reparto), s=10, alpha=0.7, label = reparto)
        migliori = dati_reparto.head(CALCIATORI_PER_CLUSTER)
        for i, (x, y, txt) in enumerate(zip(migliori['PC1'], migliori['PC2'], migliori['Known As'])):
            plt.annotate(txt, (x, y), fontsize=8, color='black')

    plt.legend(title='Reparti', loc='upper right')
    plt.title('Giocatori per reparto')
    plt.xlabel('Prima componente principale')
    plt.ylabel('Seconda componente principale')
    #plt.savefig("Clustering/grafici/reparti_PCA.png")
    plt.show()

######################################################################################################################
# Main

# Preprocessing
dataset_pca = pca() # Dataset con le componenti principali
dataset = pd.read_csv("dataset\dataset.csv") # Dataset completo
# Aggiunta colonna Reparto PC1 e PC2
dataset['Reparto'] = dataset['Best Position'].map(mappa_posizioni)
dataset["PC1"] = dataset_pca["PC1"]
dataset["PC2"] = dataset_pca["PC2"]
# Rimozione colonne inutili
colonne = ["Known As", "Best Position", "Reparto", "PC1", "PC2"]
dataset_nuovo = dataset[colonne]

# Stampa grafico posizioni
grafico_posizioni(dataset_nuovo)

# Stampa grafico reparti
grafico_reparti(dataset_nuovo)

# Stampa grafico reparti PCA
grafico_reparti_PCA(dataset_nuovo)    