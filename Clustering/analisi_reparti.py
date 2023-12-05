import pandas as pd
import matplotlib.pyplot as plt

from pca import pca
from preprocessing import MAPPA_POSIZIONI

######################################################################################################################
# COSTANTI

# Mappatura di un colore per ogni reparto
MAPPA_COLORI = {'Portiere': 'skyblue', 
                'Difensore': 'lightcoral', 
                'Centrocampista': 'lightgreen', 
                'Attaccante': 'gold'}
CALCIATORI_PER_CLUSTER = 4 # Numero di calciatori da mostrare per grafico_reparti_PCA
NUM_CALCIATORI_MIGLIORI = 30 # Numero dei migliori calciatori per grafico_migliori
REPARTI = ["Portiere", "Difensore", "Centrocampista", "Attaccante"]

######################################################################################################################
# Stampa grafico posizioni
def grafico_posizioni(dataset):

    # Conteggio delle posizioni
    conteggio_posizioni = dataset['Best Position'].value_counts()

    # Creazione grafico posizioni
    plt.figure(figsize=(8, 6))
    plt.bar(conteggio_posizioni.index, conteggio_posizioni, color=conteggio_posizioni.index.map(MAPPA_POSIZIONI).map(MAPPA_COLORI))
    
    # Aggiunta legenda e titoli
    plt.title('Conteggio per posizione')
    plt.xlabel('Posizione')
    plt.ylabel('Conteggio')
    handles = [plt.Rectangle((0, 0), 1, 1, color=MAPPA_COLORI[label]) for label in MAPPA_COLORI]
    plt.legend(handles, MAPPA_COLORI.keys(), title='Reparto', loc='upper right')
    
    #plt.savefig("Clustering/grafici/posizioni.png")
    plt.show()

######################################################################################################################
# Stampa grafico reparti
def grafico_reparti(dataset):

    # Conteggio dei reparti
    conteggio_reparti = dataset['Reparto'].value_counts()

    # Creazione grafico reparti
    plt.figure(figsize=(8, 6))
    plt.bar(conteggio_reparti.index, conteggio_reparti, color=conteggio_reparti.index.map(MAPPA_COLORI))
    
    # Aggiunta legenda e titoli
    plt.title('Conteggio per Reparto')
    plt.xlabel('Reparto')
    plt.ylabel('Conteggio')

    #plt.savefig("Clustering/grafici/reparti.png")
    plt.show()

######################################################################################################################
# Stampa grafico reparti PCA
def grafico_reparti_PCA(dataset):

    plt.figure(figsize=(6, 5))

    for reparto in REPARTI:

        dati_reparto = dataset[dataset['Reparto'] == reparto]
        plt.scatter(dati_reparto['PC1'], dati_reparto['PC2'], c=MAPPA_COLORI.get(reparto), s=10, alpha=0.7, label = reparto)
        migliori = dati_reparto.head(CALCIATORI_PER_CLUSTER)

        for i, (x, y, txt) in enumerate(zip(migliori['PC1'], migliori['PC2'], migliori['Known As'])):

            plt.annotate(txt, (x, y), fontsize=8, color='black')

    # Aggiunta legenda e titoli
    plt.legend(title='Reparti', loc='upper right')
    plt.title('Giocatori per reparto')
    plt.xlabel('Prima componente principale')
    plt.ylabel('Seconda componente principale')

    #plt.savefig("Clustering/grafici/reparti_PCA.png")
    plt.show()

######################################################################################################################
# Stampa grafico reparti PCA 3d
def grafico_reparti_PCA_3d(dataset):

    fig = plt.figure(figsize=(8, 7))
    ax = fig.add_subplot(111, projection='3d')

    for reparto in REPARTI:

        dati_reparto = dataset[dataset['Reparto'] == reparto]
        ax.scatter(dati_reparto['PC1'], dati_reparto['PC2'], dati_reparto['PC3'], c=MAPPA_COLORI.get(reparto), s=10, alpha=0.7, label = reparto)
        migliori = dati_reparto.head(CALCIATORI_PER_CLUSTER)

        for i, (x, y, z, txt) in enumerate(zip(migliori['PC1'], migliori['PC2'], migliori["PC3"], migliori['Known As'])):

            ax.text(x, y, z, txt, fontsize=8, color='black')

    # Aggiunta legenda e titoli
    ax.legend(title='Reparti', loc='upper right')
    ax.set_title('Giocatori per reparto')
    ax.set_xlabel('Prima componente principale')
    ax.set_ylabel('Seconda componente principale')
    ax.set_zlabel('Terza componente principale')

    #plt.savefig("Clustering/grafici/reparti_PCA_3d.png")
    plt.show()

######################################################################################################################
# Creazione grafico migliori calciatori
def grafico_migliori_calciatori(dataset):

    plt.figure(figsize=(6, 6))

    for index, player in dataset.iterrows():

        plt.axhline(y=player['Known As'], color='red', linestyle='--', linewidth=1, alpha=0.8)
        plt.scatter(player['Reparto'], player['Known As'], color=MAPPA_COLORI[player["Reparto"]], s=40)

    # Aggiunta legenda e titoli
    plt.title(f'Reparti dei migliori {NUM_CALCIATORI_MIGLIORI} calciatori')
    plt.xlabel('Reparto')
    plt.ylabel('Nome Giocatore')

    #plt.savefig("Clustering/grafici/reparto_migliori.png")
    plt.show()

######################################################################################################################
# Metodo principale per la creazione di tutti i grafici dell'analisi dei reparti
def analisi_reparti():

    dataset = pd.read_csv("dataset\dataset_clustering.csv")
    dataset_pca = pd.read_csv("dataset\dataset_pca.csv")

    # Aggiunta colonna PC1 PC2 e PC3
    dataset["PC1"] = dataset_pca["PC1"]
    dataset["PC2"] = dataset_pca["PC2"]
    dataset["PC3"] = dataset_pca["PC3"]

    # Rimozione colonne inutili
    colonne = ["Known As", "Best Position", "Reparto", "PC1", "PC2", "PC3"]
    dataset_nuovo = dataset[colonne]

    # Stampa grafico posizioni
    grafico_posizioni(dataset_nuovo)

    # Stampa grafico reparti
    grafico_reparti(dataset_nuovo)

    # Stampa grafico reparti PCA
    grafico_reparti_PCA(dataset_nuovo) 
    grafico_reparti_PCA_3d(dataset_nuovo)  

    # Creazione grafico migliori calciatori
    migliori = dataset.head(NUM_CALCIATORI_MIGLIORI).iloc[::-1]

    # Creazione grafico dei migliori calciatori
    grafico_migliori_calciatori(migliori)