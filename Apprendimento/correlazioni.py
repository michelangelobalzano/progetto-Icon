import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

# lettura del dataset
dataset = pd.read_csv("dataset\dataset.csv")

# colonne del quale verificare le correlazioni
colonne = ['Overall','Crossing','Finishing','Heading Accuracy','Short Passing','Volleys','Dribbling','Curve','Freekick Accuracy','LongPassing','BallControl','Acceleration','Sprint Speed','Agility','Reactions','Balance','Shot Power','Jumping','Stamina','Strength','Long Shots','Aggression','Interceptions','Positioning','Vision','Penalties','Composure','Marking','Standing Tackle','Sliding Tackle','Goalkeeper Diving','Goalkeeper Handling','Goalkeeper Kicking','Goalkeeper Positioning','Goalkeeper Reflexes']

# rimozione delle colonne che non servono
dataset_troncato = dataset[colonne]

correlazioni = dataset_troncato.corr()

print(correlazioni['Overall'].sort_values(ascending=False))

attributi = ['Overall', 'Reactions', 'Composure', 'Shot Power', 'Vision', 'Short Passing']
scatter_matrix(dataset_troncato[attributi], figsize=(15,12))
plt.show()