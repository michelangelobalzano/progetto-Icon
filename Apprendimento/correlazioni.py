import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

# lettura del dataset
dataset = pd.read_csv("dataset\dataset.csv")

# colonne del quale verificare le correlazioni
colonne = ['Overall','Crossing','Finishing','Heading Accuracy','Short Passing','Volleys','Dribbling','Curve','Freekick Accuracy','LongPassing','BallControl','Acceleration','Sprint Speed','Agility','Reactions','Balance','Shot Power','Jumping','Stamina','Strength','Long Shots','Aggression','Interceptions','Positioning','Vision','Penalties','Composure','Marking','Standing Tackle','Sliding Tackle','Goalkeeper Diving','Goalkeeper Handling','Goalkeeper Kicking','Goalkeeper Positioning','Goalkeeper Reflexes']

# rimozione delle colonne che non servono
dataset_troncato = dataset[colonne]

# ricerca delle correlazioni
correlazioni = dataset_troncato.corr()

# selezione dei migliori 5 attributi
attributi = ['Overall', 'Reactions', 'Composure', 'Shot Power', 'Vision', 'Short Passing']

# creazione del grafico
scatter_matrix(dataset_troncato[attributi], figsize=(10,10))
plt.savefig("Apprendimento/grafici/correlazioni.png")
plt.show()