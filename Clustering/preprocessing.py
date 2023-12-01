from sklearn.model_selection import train_test_split # per splittare in due sezioni il dataset
import pandas as pd

######################################################################################################################
# Preprocessing del dataset
def preprocessing():

    # lettura del dataset
    dataset = pd.read_csv("dataset\dataset.csv")

    # attrubuti da lasciare
    colonne = ['Known As', 'Crossing','Finishing','Heading Accuracy','Short Passing', 'Volleys',
               'Dribbling','Curve','Freekick Accuracy','LongPassing','BallControl',
               'Acceleration','Sprint Speed','Agility','Reactions','Balance','Shot Power',
               'Jumping','Stamina','Strength','Long Shots','Aggression','Interceptions',
               'Positioning','Vision','Penalties','Composure','Marking','Standing Tackle',
               'Sliding Tackle', 'Goalkeeper Diving', 'Goalkeeper Handling',
               'Goalkeeper Kicking', 'Goalkeeper Positioning', 'Goalkeeper Reflexes']

    # rimozione delle colonne che non servono
    dataset_troncato = dataset[colonne]

    # esportare il dataset su file
    dataset_troncato.to_csv("dataset\dataset_clustering.csv", index = False)

    return dataset_troncato