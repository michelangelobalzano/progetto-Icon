import pandas as pd
import matplotlib.pyplot as plt
from prettytable import PrettyTable

from sklearn.cluster import KMeans
from sklearn.metrics.cluster import fowlkes_mallows_score
from sklearn.metrics import adjusted_rand_score, rand_score

from analisi_reparti import MAPPA_COLORI, REPARTI, NUM_CALCIATORI_MIGLIORI
from pca import pca

######################################################################################################################
# COSTANTI

NUM_CLUSTERS = 4 # Numero di clusters
CALCIATORI_PER_CLUSTER = 4 # Calciatori da mostrare per grafico_cluster

######################################################################################################################
# Creazione grafico dei cluster
def grafico_cluster(dataset, centroidi):
    
    plt.figure(figsize=(6, 5))

    for rep in REPARTI:

        dati_cluster = dataset[dataset['Cluster'] == rep]
        plt.scatter(dati_cluster['PC1'], dati_cluster['PC2'], c=MAPPA_COLORI.get(rep), s=10, alpha=0.7, label=f'{rep}')
        migliori = dati_cluster.head(CALCIATORI_PER_CLUSTER)

        for i, (x, y, txt) in enumerate(zip(migliori['PC1'], migliori['PC2'], migliori['Known As'])):

            plt.annotate(txt, (x, y), fontsize=8, color='black')

    # Aggiunta centroidi
    plt.scatter(centroidi[:, 0], centroidi[:, 1], c='black', marker='.', s=20, label='Centroidi')

    # Aggiunta legenda e titoli
    plt.legend(title='Clusters', loc='upper right')
    plt.title('K-Means Clustering')
    plt.xlabel('Prima componente principale')
    plt.ylabel('Seconda componente principale')

    #plt.savefig("Clustering/grafici/k_means.png")
    plt.show()

######################################################################################################################
# Creazione grafico dei cluster 3d
def grafico_cluster_3d(dataset, centroidi):

    fig = plt.figure(figsize=(8, 7))
    ax = fig.add_subplot(111, projection='3d')

    for rep in REPARTI:

        dati_cluster = dataset[dataset['Cluster'] == rep]
        ax.scatter(dati_cluster['PC1'], dati_cluster['PC2'], dati_cluster['PC3'], c=MAPPA_COLORI.get(rep), s=10, alpha=0.7, label=f'{rep}')
        migliori = dati_cluster.head(CALCIATORI_PER_CLUSTER)

        for i, (x, y, z, txt) in enumerate(zip(migliori['PC1'], migliori['PC2'], migliori['PC3'], migliori['Known As'])):

            ax.text(x, y, z, txt, fontsize=8, color='black')

    # Aggiunta centroidi
    ax.scatter(centroidi[:, 0], centroidi[:, 1], centroidi[:, 2], c='black', marker='.', s=20, label='Centroidi')

    # Aggiunta legenda e titoli
    ax.legend(title='Clusters', loc='upper right')
    ax.set_title('K-Means Clustering')
    ax.set_xlabel('Prima componente principale')
    ax.set_ylabel('Seconda componente principale')
    ax.set_zlabel('Terza componente principale')

    #plt.savefig("Clustering/grafici/k_means_3d.png")
    plt.show()

######################################################################################################################
# Creazione grafico migliori calciatori
def grafico_migliori_calciatori(dataset):

    plt.figure(figsize=(6, 6))

    for rep in REPARTI:

        dati_cluster = dataset[dataset['Cluster'] == rep]
        plt.scatter(dati_cluster['Cluster'], dati_cluster['Known As'], color=MAPPA_COLORI.get(rep), s=40)

        # Aggiunta delle linee orizzontali tratteggiate per ogni calciatore
        for index, row in dati_cluster.iterrows():

            plt.axhline(y=row['Known As'], linestyle='--', color='gray', alpha=0.5)
    
    # Aggiunta legenda e titoli
    plt.title(f'K-means clustering migliori {NUM_CALCIATORI_MIGLIORI} calciatori')
    plt.xlabel('Cluster')
    plt.ylabel('Nome Giocatore')

    #plt.savefig("Clustering/grafici/hierarchical_migliori.png")
    plt.show()

######################################################################################################################
# Metodo che associa ai numeri di cluster un reparto corrispondente
def associazione_reparto_cluster(dataset):
    
    for rep in REPARTI:

        dati_reparto = dataset[dataset["Reparto"] == rep]
        cluster = dati_reparto["Cluster"].value_counts().idxmax()
        dataset["Cluster"] = dataset["Cluster"].replace(cluster, rep)
    
    return dataset

######################################################################################################################
# Metodo di valutazione del clustering
def valutazione(etichette, assegnazioni):

    ri = rand_score(etichette, assegnazioni)
    ari = adjusted_rand_score(etichette, assegnazioni)
    fmi = fowlkes_mallows_score(etichette, assegnazioni)

    tabella = PrettyTable(["Indice", "Punteggio"])

    tabella.add_row(["Rand Index (RI)", round(ri, 2)])
    tabella.add_row(["Adjusted Rand Index (ARI)", round(ari, 2)])
    tabella.add_row(["Fowlkes Mallows Index (FMI)", round(fmi, 2)])

    print(tabella)

######################################################################################################################
# K-means intero dataset
def k_means_clustering():

    # Lettura del dataset della PCA
    dataset = pd.read_csv("dataset\dataset_pca.csv")

    # Creazione del modello di clustering
    kmeans = KMeans(n_clusters=NUM_CLUSTERS, n_init=10)
    kmeans.fit(dataset.iloc[:, :-3])

    # Aggiunta della colonna Cluster al dataset
    dataset['Cluster'] = kmeans.labels_

    # Associazione dei reparti ai numeri di cluster
    dataset = associazione_reparto_cluster(dataset)
    
    # Acquisizione punti centroidi dei clusters
    centroidi = kmeans.cluster_centers_

    # Creazione grafici dei clusters
    grafico_cluster(dataset, centroidi)
    grafico_cluster_3d(dataset, centroidi)

    # Creazione grafico migliori calciatori
    migliori = dataset.head(NUM_CALCIATORI_MIGLIORI).iloc[::-1]
    grafico_migliori_calciatori(migliori)

    # Valutazione dei risultati della classificazione
    valutazione(dataset["Reparto"], dataset["Cluster"])