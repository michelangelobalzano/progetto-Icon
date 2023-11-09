from sklearn.model_selection import train_test_split # per splittare in due sezioni il dataset
import pandas as pd

def preprocessing():
    # lettura del dataset
    dataset = pd.read_csv("dataset\dataset.csv")

    # attrubuti da lasciare
    colonne = ['Overall','Crossing','Finishing','Heading Accuracy','Short Passing','Volleys','Dribbling','Curve','Freekick Accuracy','LongPassing','BallControl','Acceleration','Sprint Speed','Agility','Reactions','Balance','Shot Power','Jumping','Stamina','Strength','Long Shots','Aggression','Interceptions','Positioning','Vision','Penalties','Composure','Marking','Standing Tackle','Sliding Tackle']

    # rimozione dei portieri
    dataset = dataset[dataset['Best Position'] != 'GK']

    # rimozione delle colonne che non servono
    dataset_troncato = dataset[colonne]

    # esportare il dataset su file
    # dataset_troncato.to_csv("dataset\dataset_troncato.csv", index = False)

    # creazione training set (80%) e test set (20%)
    training_set, test_set = train_test_split(dataset_troncato, test_size=0.2)

    # creazione tabelle dell'attributo target
    training_set_target = training_set['Overall']
    test_set_target = test_set['Overall']

    # creazione tabelle degli attributi di input
    training_set_input = training_set.drop('Overall', axis=1)
    test_set_input = test_set.drop('Overall', axis=1)

    return training_set_input, training_set_target, test_set_input, test_set_target