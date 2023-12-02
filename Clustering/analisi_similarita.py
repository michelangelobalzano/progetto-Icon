from pca import pca
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import euclidean_distances

NUMERO_CALCIATORI_SIMILI = 10

def grafico_similarita(calciatori_simili, calciatore, nome):
    # Creazione di uno scatter plot nello spazio delle componenti principali
    plt.figure(figsize=(6, 5))

    # Plot di tutti i calciatori
    plt.scatter(calciatori_simili["PC1"], calciatori_simili["PC2"], label='Altri Calciatori')

    # Plot di Messi con un colore diverso
    plt.scatter(calciatore["PC1"], calciatore["PC2"], color='red', label=nome)

    # Annotazioni per i calciatori più simili
    for index, player in calciatori_simili.iterrows():
        plt.annotate(player['Known As'], (player["PC1"], player["PC2"]))

    plt.title('Scatter Plot dei Calciatori Simili a Messi (PCA)')
    plt.xlabel('Componente Principale 1')
    plt.ylabel('Componente Principale 2')
    plt.legend()
    plt.savefig(f"Clustering/grafici/simili_{nome}.png")
    plt.show()

def analisi_similarita(nome):

    dataset = pca()

    calciatore = dataset[dataset['Known As'] == nome]
    calciatore = calciatore.drop(['Known As'], axis=1)

    componenti = dataset.drop(['Known As'], axis=1)

    distanze = euclidean_distances(calciatore, componenti)

    indici_calciatori_simili = distanze.argsort()[0][:NUMERO_CALCIATORI_SIMILI]

    calciatori_simili = dataset.iloc[indici_calciatori_simili]

    grafico_similarita(calciatori_simili, calciatore, nome)