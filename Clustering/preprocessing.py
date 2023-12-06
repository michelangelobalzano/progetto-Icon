import pandas as pd

######################################################################################################################
# COSTANTI

# Mappatura di ogni posizione in un reparto
MAPPA_POSIZIONI = {'GK': 'Portiere',
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

# attrubuti per la pca
ATTRIBUTI = ['Crossing','Finishing','Heading Accuracy','Short Passing', 'Volleys',
            'Dribbling','Curve','Freekick Accuracy','LongPassing','BallControl',
            'Acceleration','Sprint Speed','Agility','Reactions','Balance','Shot Power',
            'Jumping','Stamina','Strength','Long Shots','Aggression','Interceptions',
            'Positioning','Vision','Penalties','Composure','Marking','Standing Tackle',
            'Sliding Tackle', 'Goalkeeper Diving', 'Goalkeeper Handling',
            'Goalkeeper Kicking', 'Goalkeeper Positioning', 'Goalkeeper Reflexes']

######################################################################################################################
# Metodo di associazione di un reparto ad una posizione
def mappa_posizione(posizione):

    return MAPPA_POSIZIONI.get(posizione)

######################################################################################################################
# Preprocessing del dataset
def preprocessing():

    # lettura del dataset
    dataset = pd.read_csv("dataset\dataset.csv")

    # rimozione delle colonne che non servono
    dataset_troncato = dataset[ATTRIBUTI]
    dataset_troncato["Known As"] = dataset["Known As"]
    dataset_troncato["Best Position"] = dataset["Best Position"]

    # Aggiunta della colonna Reparto
    dataset_troncato['Reparto'] = dataset['Best Position'].map(MAPPA_POSIZIONI)

    return dataset_troncato