import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster, set_link_color_palette
import matplotlib.pyplot as plt
from pca import pca

NUM_CLUSTERS = 4 # Numero di clusters
CALCIATORI_PER_CLUSTER = 4 # Calciatori da mostrare per grafico_cluster
NUM_CALCIATORI_MIGLIORI = 30 # Migliori calciatori per grafico_migliori
# Mappa dei colori per cluster
mappa_colori = {0: 'lightgreen', 
                1: 'skyblue', 
                2: 'lightcoral', 
                3: 'gold'}

######################################################################################################################
# Creazione grafico dei cluster
def grafico_cluster(dataset):
    
    plt.figure(figsize=(6, 5))
    for num_cluster in range(NUM_CLUSTERS):
        dati_cluster = dataset[dataset['Cluster'] == num_cluster]
        plt.scatter(dati_cluster['PC1'], dati_cluster['PC2'], c=mappa_colori.get(num_cluster), s=10, alpha=0.7, label=f'Cluster {num_cluster + 1}')
        migliori = dati_cluster.head(CALCIATORI_PER_CLUSTER)
        for i, (x, y, txt) in enumerate(zip(migliori['PC1'], migliori['PC2'], migliori['Known As'])):
            plt.annotate(txt, (x, y), fontsize=8, color='black')
    # Aggiunta legenda e titoli
    plt.legend(title='Clusters', loc='upper right')
    plt.title('Hierarchical Clustering')
    plt.xlabel('Prima componente principale')
    plt.ylabel('Seconda componente principale')
    plt.savefig("Clustering/grafici/hierarchical_clustering.png")
    plt.show()

######################################################################################################################
# Creazione grafico dei cluster 3d
def grafico_cluster_3d(dataset):
    
    fig = plt.figure(figsize=(8, 7))
    ax = fig.add_subplot(111, projection='3d')
    for num_cluster in range(NUM_CLUSTERS):
        dati_cluster = dataset[dataset['Cluster'] == num_cluster]
        ax.scatter(dati_cluster['PC1'], dati_cluster['PC2'], dati_cluster['PC3'], c=mappa_colori.get(num_cluster), s=10, alpha=0.7, label=f'Cluster {num_cluster + 1}')
        migliori = dati_cluster.head(CALCIATORI_PER_CLUSTER)
        for i, (x, y, z, txt) in enumerate(zip(migliori['PC1'], migliori['PC2'], migliori['PC3'], migliori['Known As'])):
            ax.text(x, y, z, txt, fontsize=8, color='black')
    # Aggiunta legenda e titoli
    ax.legend(title='Clusters', loc='upper right')
    ax.set_title('Hierarchical Clustering')
    ax.set_xlabel('Prima componente principale')
    ax.set_ylabel('Seconda componente principale')
    ax.set_zlabel('Terza componente principale')
    plt.savefig("Clustering/grafici/hierarchical_clustering_3d.png")
    plt.show()

######################################################################################################################
# Creazione grafico dendogramma
def dendogramma(linkage_matrix):

    plt.figure(figsize=(7, 5))
    cut_height = linkage_matrix[-NUM_CLUSTERS + 1, 2]
    cluster_labels = fcluster(linkage_matrix, t=cut_height, criterion='distance')

    # Colora i sottoalberi in base alle etichette di cluster e alla mappa di colori personalizzata
    dendrogram(linkage_matrix, 
               no_labels=True, 
               orientation='top', 
               distance_sort='descending', 
               show_leaf_counts=True,
               color_threshold=cut_height)
    plt.axhline(y=cut_height, color='red', linestyle='--')
    plt.title('Dendrogramma del clustering gerarchico')
    plt.xticks([])
    plt.xlabel('Giocatori')
    plt.ylabel('Distanza Euclidea')
    plt.savefig("Clustering/grafici/dendogramma.png")
    plt.show()

######################################################################################################################
# Hierarchical clustering
def hierarchical_clustering(dataset):

    # Creazione del modello di clustering
    model = AgglomerativeClustering(n_clusters=NUM_CLUSTERS, affinity='euclidean', linkage='ward')
    labels = model.fit_predict(dataset.iloc[:, :-1])
    
    # Definizione della matrice di collegamento per il dendogramma
    linkage_matrix = linkage(dataset.iloc[:, :-1], method='ward', metric='euclidean')

    # Aggiunta della colonna Cluster al dataset
    dataset['Cluster'] = labels

    # Creazione grafici dei clusters
    grafico_cluster(dataset)
    grafico_cluster_3d(dataset)

    # Creazione grafico dendogramma
    dendogramma(linkage_matrix)

######################################################################################################################
# Metodo principale per la creazione dei grafici di clustering
def hc_clustering():

    dataset_pca = pca()

    hierarchical_clustering(dataset_pca)