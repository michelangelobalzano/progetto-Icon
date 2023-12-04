from sklearn.cluster import KMeans
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
def grafico_cluster(dataset, centroidi):
    plt.figure(figsize=(6, 5))
    for num_cluster in range(NUM_CLUSTERS):
        dati_cluster = dataset[dataset['Cluster'] == num_cluster]
        plt.scatter(dati_cluster['PC1'], dati_cluster['PC2'], c=mappa_colori.get(num_cluster), s=10, alpha=0.7, label=f'Cluster {num_cluster + 1}')
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
    for num_cluster in range(NUM_CLUSTERS):
        dati_cluster = dataset[dataset['Cluster'] == num_cluster]
        ax.scatter(dati_cluster['PC1'], dati_cluster['PC2'], dati_cluster['PC3'], c=mappa_colori.get(num_cluster), s=10, alpha=0.7, label=f'Cluster {num_cluster + 1}')
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
    for index, player in dataset.iterrows():
        plt.axhline(y=player['Known As'], color='red', linestyle='--', linewidth=1, alpha=0.8)
        plt.scatter(player['Cluster'], player['Known As'], color=mappa_colori[player["Cluster"]], s=40)
    plt.title(f'Clustering dei migliori {NUM_CALCIATORI_MIGLIORI} calciatori')
    plt.xlabel('Cluster')
    plt.ylabel('Nome Giocatore')
    #plt.savefig("Clustering/grafici/cluster_migliori.png")
    plt.show()

######################################################################################################################
# K-means intero dataset
def k_means(dataset):

    # Creazione del modello di clustering
    kmeans = KMeans(n_clusters=NUM_CLUSTERS, n_init=10)
    kmeans.fit(dataset.iloc[:, :-1])

    # Aggiunta della colonna Cluster al dataset
    dataset['Cluster'] = kmeans.labels_

    # Acquisizione punti centroidi dei clusters
    centroidi = kmeans.cluster_centers_

    # Creazione grafico dei clusters
    grafico_cluster(dataset, centroidi)
    grafico_cluster_3d(dataset, centroidi)

    # Creazione grafico migliori calciatori
    migliori = dataset.head(NUM_CALCIATORI_MIGLIORI).iloc[::-1]

    # Creazione grafico dei migliori calciatori
    grafico_migliori_calciatori(migliori)
    
######################################################################################################################
# Metodo principale per la creazione dei grafici di clustering
def clustering():

    dataset_pca = pca()

    k_means(dataset_pca)
    
    