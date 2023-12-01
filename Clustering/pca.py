from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np
from creazione_grafici import grafico_vs, grafico_vsc
import pandas as pd
from preprocessing import preprocessing

######################################################################################################################
# PCA
def pca():

    dataset = preprocessing()

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
    # grafico_vs(varianza_spiegata)

    # Stampa grafico varianza spiegata cumulativa
    # grafico_vsc(varianza_spiegata_cumulativa)

    # Calcolo del numero di componenti nel 95% di spiegazione della varianza
    num_componenti = (varianza_spiegata_cumulativa < 0.95).sum() + 1

    # PCA con il numero di componenti
    pca = PCA(n_components=num_componenti)
    componenti_principali = pca.fit_transform(componenti)

    # Creazione nuovo dataset con le componenti principali
    dataset_pca = pd.DataFrame(data=componenti_principali, columns=[f'PC{i}' for i in range(1, num_componenti + 1)])
    dataset_pca["Known As"] = dataset["Known As"]

    dataset_pca.to_csv("dataset\dataset_pca.csv", index = False)
    
    return dataset_pca