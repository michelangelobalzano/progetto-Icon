from pca import pca
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import euclidean_distances

NUMERO_CALCIATORI_SIMILI = 10

######################################################################################################################
# Stampa grafico dei 10 calciatori più simili
def grafico_similarita(calciatori_simili, calciatore, nome):

    # Creazione di uno scatter plot nello spazio delle componenti principali
    plt.figure(figsize=(6, 5))

    # Plot di tutti i calciatori
    plt.scatter(calciatori_simili["PC1"], calciatori_simili["PC2"], label='Altri calciatori')

    # Plot di Messi con un colore diverso
    plt.scatter(calciatore["PC1"], calciatore["PC2"], color='red', label=nome)

    # Annotazioni per i calciatori più simili
    for index, player in calciatori_simili.iterrows():
        plt.annotate(player['Known As'], (player["PC1"], player["PC2"]))

    plt.title(f'10 calciatori più simili a {nome}')
    plt.xlabel('Prima componente principale')
    plt.ylabel('Seconda componente principale')
    plt.legend()
    #plt.savefig(f"Clustering/grafici/simili_{nome}.png")
    plt.show()

######################################################################################################################
# Stampa grafico dei 10 calciatori più simili in 3d
def grafico_similarita_3d(calciatori_simili, calciatore, nome):
    
    # Creazione di uno scatter plot nello spazio delle componenti principali
    fig = plt.figure(figsize=(8, 7))
    ax = fig.add_subplot(111, projection='3d')

    # Plot di tutti i calciatori
    ax.scatter(calciatori_simili["PC1"], calciatori_simili["PC2"], calciatori_simili["PC3"], label='Altri calciatori', s=20)

    # Plot di Messi con un colore diverso
    ax.scatter(calciatore["PC1"], calciatore["PC2"], calciatore["PC3"], color='red', label=nome, s=50)

    # Annotazioni per i calciatori più simili
    for index, player in calciatori_simili.iterrows():
        ax.text(player["PC1"], player["PC2"], player["PC3"], player['Known As'], fontsize=8)

    ax.set_title(f'10 calciatori più simili a {nome}')
    ax.set_xlabel('Prima componente principale')
    ax.set_ylabel('Seconda componente principale')
    ax.set_zlabel('Terza componente principale')
    ax.legend()

    #plt.savefig(f"Clustering/grafici/simili_{nome}_3d.png")
    plt.show()

######################################################################################################################
# Metodo principale per la ricerca di similarita
def analisi_similarita(nome):

    dataset = pca()

    calciatore = dataset[dataset['Known As'] == nome]
    calciatore = calciatore.drop(['Known As'], axis=1)

    componenti = dataset.drop(['Known As'], axis=1)

    distanze = euclidean_distances(calciatore, componenti)

    indici_calciatori_simili = distanze.argsort()[0][:NUMERO_CALCIATORI_SIMILI]

    calciatori_simili = dataset.iloc[indici_calciatori_simili]

    grafico_similarita(calciatori_simili, calciatore, nome)
    grafico_similarita_3d(calciatori_simili, calciatore, nome)