from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

NUM_CLUSTERS = 4 # Numero di clusters
CALCIATORI_PER_CLUSTER = 4 # Calciatori da mostrare per cluster
# Mappa dei colori per cluster
mappa_colori = {0: 'lightgreen', 
                1: 'skyblue', 
                2: 'lightcoral', 
                3: 'gold'}

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

    # Ordinamento del dataset per Cluster e per prima componente principale
    dataset = dataset.sort_values(by=['Cluster', 'PC1'], ascending=[True, True])

    # Creazione grafico dei clusters
    for num_cluster in range(NUM_CLUSTERS):
        dati_cluster = dataset[dataset['Cluster'] == num_cluster]
        plt.scatter(dati_cluster['PC1'], dati_cluster['PC2'], c=mappa_colori.get(num_cluster), s=10, alpha=0.7, label=f'Cluster {num_cluster + 1}')
        migliori = dati_cluster.head(CALCIATORI_PER_CLUSTER)
        for i, (x, y, txt) in enumerate(zip(migliori['PC1'], migliori['PC2'], migliori['Known As'])):
            plt.annotate(txt, (x, y), fontsize=8, color='black')

    # Aggiunta centroidi
    plt.scatter(centroidi[:, 0], centroidi[:, 1], c='black', marker='.', s=20, label='Centroidi')

    plt.legend(title='Clusters', loc='upper right')
    plt.title('K-Means Clustering')
    plt.xlabel('Prima componente principale')
    plt.ylabel('Seconda componente principale')
    #plt.savefig("Clustering/grafici/k_means.png")
    plt.show()