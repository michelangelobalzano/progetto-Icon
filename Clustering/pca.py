from sklearn.decomposition import PCA
from preprocessing import preprocessing
import numpy as np
from creazione_grafici import grafico_vs, grafico_vsc
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd

dataset, nomi_giocatori = preprocessing()

# PCA
pca = PCA()
pca.fit(dataset)

# Calcolo varianza spiegata
varianza_spiegata = pca.explained_variance_
# Normalizzazione varianza spiegata nell'intervallo [0; 1]
varianza_spiegata = varianza_spiegata / sum(varianza_spiegata)
# Calcolo varianza spiegata cumulativa
varianza_spiegata_cumulativa = np.cumsum(varianza_spiegata)

# Stampa grafico varianza spiegata
# grafico_vs(varianza_spiegata)

# Stampa grafico varianza spiegata cumulativa
# grafico_vsc(varianza_spiegata_cumulativa)

num_componenti = (varianza_spiegata_cumulativa < 0.95).sum() + 1

# Usa n_components nel tuo modello PCA
pca = PCA(n_components=num_componenti)
componenti_principali = pca.fit_transform(dataset)

# Crea un DataFrame con le componenti principali
pc_df = pd.DataFrame(data=componenti_principali, columns=[f'PC{i}' for i in range(1, num_componenti + 1)])

# Aggiungi il nome del giocatore al DataFrame delle componenti principali
pc_df['Nome_Giocatore'] = nomi_giocatori

# Creazione del modello di clustering
kmeans = KMeans(n_clusters=4)
kmeans.fit(pc_df.iloc[:, :-1])

# Aggiungi le etichette dei cluster al DataFrame
pc_df['Cluster'] = kmeans.labels_

pc_df.to_csv("dataset\dataset_pca.csv", index = False)

# Ordina il DataFrame per il cluster e altre metriche di tuo interesse
pc_df_sorted = pc_df.sort_values(by=['Cluster', 'PC1'], ascending=[True, True])

scatter = plt.scatter(pc_df_sorted['PC1'], pc_df_sorted['PC2'], c=pc_df_sorted['Cluster'], cmap='viridis', label='Cluster')
plt.title('PCA + K-Means Clustering')
plt.xlabel('PC1')
plt.ylabel('PC2')

# Aggiungi legenda per i cluster
plt.legend(title='Cluster', loc='upper right')

# Aggiungi linee e annota i nomi dei giocatori per cluster senza sovrapposizioni
for cluster_num in range(4):  # Modifica in base al numero di cluster che hai specificato
    cluster_data = pc_df_sorted[pc_df_sorted['Cluster'] == cluster_num].head(5)
    for i, (x, y, txt) in enumerate(zip(cluster_data['PC1'], cluster_data['PC2'], cluster_data['Nome_Giocatore'])):
        plt.annotate(txt, (x, y), fontsize=8, color='black', xytext=(5, 5), textcoords='offset points')
        
        # Calcola la direzione della linea
        dx, dy = x + 0.5 - x, y + 0.5 - y
        
        # Verifica se la linea va verso l'interno del grafico
        if x + dx < plt.xlim()[0]:
            dx = plt.xlim()[0] - x
        if x + dx > plt.xlim()[1]:
            dx = plt.xlim()[1] - x
        if y + dy < plt.ylim()[0]:
            dy = plt.ylim()[0] - y
        if y + dy > plt.ylim()[1]:
            dy = plt.ylim()[1] - y
        
        plt.plot([x, x + dx], [y, y + dy], linestyle='--', color='gray', linewidth=0.5)

plt.show()

'''# Visualizza i risultati
plt.scatter(pc_df['PC1'], pc_df['PC2'], c=pc_df['Cluster'], cmap='viridis')
plt.title('PCA + K-Means Clustering')
plt.xlabel('PC1')
plt.ylabel('PC2')

plt.show()'''