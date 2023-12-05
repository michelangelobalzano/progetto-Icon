import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.metrics import adjusted_rand_score
from sklearn.metrics import jaccard_score
from sklearn.metrics.cluster import fowlkes_mallows_score

from pca import pca
from analisi_reparti import MAPPA_COLORI, REPARTI

######################################################################################################################
# COSTANTI

NUM_CLUSTERS = 4 # Numero di clusters
CALCIATORI_PER_CLUSTER = 4 # Calciatori da mostrare per grafico_cluster
NUM_CALCIATORI_MIGLIORI = 30 # Migliori calciatori per grafico_migliori

######################################################################################################################
# Creazione grafico dei cluster
def grafico_cluster(dataset):
    
    plt.figure(figsize=(6, 5))

    for rep in REPARTI:

        dati_cluster = dataset[dataset['Cluster'] == rep]
        plt.scatter(dati_cluster['PC1'], dati_cluster['PC2'], c=MAPPA_COLORI.get(rep), s=10, alpha=0.7, label=f'{rep}')
        migliori = dati_cluster.head(CALCIATORI_PER_CLUSTER)

        for i, (x, y, txt) in enumerate(zip(migliori['PC1'], migliori['PC2'], migliori['Known As'])):

            plt.annotate(txt, (x, y), fontsize=8, color='black')

    # Aggiunta legenda e titoli
    plt.legend(title='Clusters', loc='upper right')
    plt.title('Hierarchical Clustering')
    plt.xlabel('Prima componente principale')
    plt.ylabel('Seconda componente principale')

    #plt.savefig("Clustering/grafici/hierarchical_clustering.png")
    plt.show()

######################################################################################################################
# Creazione grafico dei cluster 3d
def grafico_cluster_3d(dataset):
    
    fig = plt.figure(figsize=(8, 7))
    ax = fig.add_subplot(111, projection='3d')

    for rep in REPARTI:

        dati_cluster = dataset[dataset['Cluster'] == rep]
        ax.scatter(dati_cluster['PC1'], dati_cluster['PC2'], dati_cluster['PC3'], c=MAPPA_COLORI.get(rep), s=10, alpha=0.7, label=f'{rep}')
        migliori = dati_cluster.head(CALCIATORI_PER_CLUSTER)

        for i, (x, y, z, txt) in enumerate(zip(migliori['PC1'], migliori['PC2'], migliori['PC3'], migliori['Known As'])):

            ax.text(x, y, z, txt, fontsize=8, color='black')

    # Aggiunta legenda e titoli
    ax.legend(title='Clusters', loc='upper right')
    ax.set_title('Hierarchical Clustering')
    ax.set_xlabel('Prima componente principale')
    ax.set_ylabel('Seconda componente principale')
    ax.set_zlabel('Terza componente principale')

    #plt.savefig("Clustering/grafici/hierarchical_clustering_3d.png")
    plt.show()

######################################################################################################################
# Creazione grafico dendogramma
def dendogramma(linkage_matrix):

    # Calcolo della linea di taglio
    cut_height = linkage_matrix[-NUM_CLUSTERS + 1, 2]

    # Dendogramma
    dendrogram(linkage_matrix, 
            no_labels=True, 
            orientation='top', 
            distance_sort='descending', 
            show_leaf_counts=True,
            color_threshold=cut_height)

    # Aggiungere una linea di taglio al dendrogramma
    plt.axhline(y=cut_height, color='red', linestyle='--')

    # Aggiunta legenda e titoli
    plt.title('Dendrogramma del clustering gerarchico')
    plt.xlabel('Calciatori')
    plt.ylabel('Distanza')

    #plt.savefig("Clustering/grafici/dendogramma.png")
    plt.show()

######################################################################################################################
# Creazione grafico migliori calciatori
def grafico_migliori_calciatori(dataset):

    plt.figure(figsize=(6, 6))

    for index, player in dataset.iterrows():

        plt.axhline(y=player['Known As'], color='red', linestyle='--', linewidth=1, alpha=0.8)
        plt.scatter(player['Cluster'], player['Known As'], color=MAPPA_COLORI[player["Cluster"]], s=40)
    
    # Aggiunta legenda e titoli
    plt.title(f'Clustering dei migliori {NUM_CALCIATORI_MIGLIORI} calciatori')
    plt.xlabel('Cluster')
    plt.ylabel('Nome Giocatore')

    #plt.savefig("Clustering/grafici/hierarchical_migliori.png")
    plt.show()

######################################################################################################################
# Metodo che associa ai numeri di cluster un reparto corrispondente
def associazione_reparto_cluster(dataset):

    cluster = []

    for rep in REPARTI:

        cluster.append(dataset[dataset["Reparto"] == rep]["Cluster"].value_counts().idxmax())

    for k in range(NUM_CLUSTERS):

        dataset["Cluster"] = dataset["Cluster"].replace(cluster[k], REPARTI[k])

    return dataset

######################################################################################################################
# Hierarchical clustering
def hierarchical_clustering(dataset):

    # Creazione del modello di clustering
    model = AgglomerativeClustering(n_clusters=NUM_CLUSTERS, metric='cosine', linkage='average')
    labels = model.fit_predict(dataset.iloc[:, :-3])
    
    linkage_matrix = linkage(model.children_, metric='cosine', method='average')
    
    # Aggiunta della colonna Cluster al dataset
    dataset['Cluster'] = labels

    # Associazione dei reparti ai numeri di cluster
    dataset = associazione_reparto_cluster(dataset)
    
    # Creazione grafici dei clusters
    grafico_cluster(dataset)
    grafico_cluster_3d(dataset)

    # Creazione grafico dendogramma
    dendogramma(linkage_matrix)

    # Creazione grafico migliori calciatori
    migliori = dataset.head(NUM_CALCIATORI_MIGLIORI).iloc[::-1]
    grafico_migliori_calciatori(migliori)

    return dataset["Cluster"]

######################################################################################################################
# Metodo di valutazione del clustering
def valutazione(etichette, assegnazioni):

    rand_index = adjusted_rand_score(etichette, assegnazioni)
    print (rand_index)
    jaccard_index = jaccard_score(etichette, assegnazioni, average='weighted')
    print (jaccard_index)
    fms = fowlkes_mallows_score(etichette, assegnazioni)
    print(fms)

######################################################################################################################
# Metodo principale per la creazione dei grafici di clustering
def hc_clustering():

    dataset_pca = pd.read_csv("dataset\dataset_pca.csv")

    assegnazioni = hierarchical_clustering(dataset_pca)

    valutazione(dataset_pca["Reparto"], assegnazioni)