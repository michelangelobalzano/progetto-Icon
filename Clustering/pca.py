from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from preprocessing import preprocessing

######################################################################################################################
# Grafico varianza spiegata
def grafico_vs(vs, attributi):

    plt.figure(figsize=(8, 6))
    plt.bar(range(1, len(vs) + 1), vs, align='center')
    plt.title('Varianza spiegata per componente')
    plt.xlabel('Componenti')
    plt.ylabel('Varianza spiegata')
    plt.xticks(range(1, len(vs) + 1), attributi, rotation=90)
    #plt.savefig("Clustering/grafici/varianza_spiegata.png")
    plt.show()

######################################################################################################################
# Grafico varianza spiegata cumulativa
def grafico_vsc(vsc, attributi):
    
    plt.figure(figsize=(8, 6))
    plt.plot(range(1, len(vsc) + 1), vsc, marker='o', linestyle='-', color='b')
    plt.title('Varianza cumulativa spiegata')
    plt.xlabel('Numero di componenti principali')
    plt.ylabel('Varianza cumulativa spiegata')
    plt.xticks(range(1, len(vsc) + 1), attributi, rotation=90)
    plt.axhline(y=0.95, color='r', linestyle='--', label='90% Varianza Spiegata')
    #plt.savefig("Clustering/grafici/varianza_spiegata_cumulativa.png")
    plt.show()

######################################################################################################################
# PCA
def pca():

    preprocessing()

    dataset = pd.read_csv("dataset\dataset_clustering.csv")

    componenti = dataset.select_dtypes(include=['float64', 'int64'])

    # PCA
    pca = PCA()
    pca.fit(componenti)

    # Calcolo varianza spiegata
    varianza_spiegata = pca.explained_variance_
    # Normalizzazione varianza spiegata nell'intervallo [0; 1]
    varianza_spiegata = varianza_spiegata / sum(varianza_spiegata)
    # Calcolo varianza spiegata cumulativa
    varianza_spiegata_cumulativa = np.cumsum(varianza_spiegata)

    # Stampa grafico varianza spiegata
    #grafico_vs(varianza_spiegata, attributi)

    # Stampa grafico varianza spiegata cumulativa
    #grafico_vsc(varianza_spiegata_cumulativa, attributi)

    # Calcolo del numero di componenti nel 95% di spiegazione della varianza
    num_componenti = (varianza_spiegata_cumulativa < 0.95).sum() + 1
    
    # PCA con il numero di componenti
    pca = PCA(n_components=num_componenti)
    componenti_principali = pca.fit_transform(componenti)

    # Creazione nuovo dataset con le componenti principali
    dataset_pca = pd.DataFrame(data=componenti_principali, columns=[f'PC{i}' for i in range(1, num_componenti + 1)])
    dataset_pca["Known As"] = dataset["Known As"]
    dataset_pca["Best Position"] = dataset["Best Position"]
    dataset_pca["Reparto"] = dataset["Reparto"]

    # Esportazione del dataset
    dataset_pca.to_csv("dataset\dataset_pca.csv", index = False)