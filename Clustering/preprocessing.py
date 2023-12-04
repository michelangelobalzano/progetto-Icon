from sklearn.model_selection import train_test_split # per splittare in due sezioni il dataset
import pandas as pd

# Mappatura di ogni posizione in un reparto
mappa_posizioni = {'GK': 'Portiere',
                   'CB': 'Difensore',
                   'LB': 'Difensore',
                   'RB': 'Difensore',
                   'LWB': 'Difensore',
                   'RWB': 'Difensore',
                   'CDM': 'Centrocampista',
                   'CM': 'Centrocampista',
                   'LM': 'Centrocampista',
                   'RM': 'Centrocampista',
                   'CAM': 'Attaccante',
                   'LW': 'Attaccante',
                   'RW': 'Attaccante',
                   'CF': 'Attaccante',
                   'ST': 'Attaccante'
}

def mappa_posizione(posizione):
    return mappa_posizioni.get(posizione)

######################################################################################################################
# Preprocessing del dataset
def preprocessing():

    # lettura del dataset
    dataset = pd.read_csv("dataset\dataset.csv")

    # attrubuti da lasciare
    colonne = ['Crossing','Finishing','Heading Accuracy','Short Passing', 'Volleys',
               'Dribbling','Curve','Freekick Accuracy','LongPassing','BallControl',
               'Acceleration','Sprint Speed','Agility','Reactions','Balance','Shot Power',
               'Jumping','Stamina','Strength','Long Shots','Aggression','Interceptions',
               'Positioning','Vision','Penalties','Composure','Marking','Standing Tackle',
               'Sliding Tackle', 'Goalkeeper Diving', 'Goalkeeper Handling',
               'Goalkeeper Kicking', 'Goalkeeper Positioning', 'Goalkeeper Reflexes']

    # rimozione delle colonne che non servono
    dataset_troncato = dataset[colonne]
    dataset_troncato["Known As"] = dataset["Known As"]
    dataset_troncato["Best Position"] = dataset["Best Position"]

    # Aggiunta della colonna Reparto
    dataset_troncato['Reparto'] = dataset['Best Position'].map(mappa_posizioni)

    # esportare il dataset su file
    dataset_troncato.to_csv("dataset\dataset_clustering.csv", index = False)