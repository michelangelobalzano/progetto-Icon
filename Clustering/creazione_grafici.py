import matplotlib.pyplot as plt

# Nomi degli attributi da mostrare sui grafici
attribute_names = ['Crossing','Finishing','Heading Accuracy','Short Passing', 'Volleys',
               'Dribbling','Curve','Freekick Accuracy','LongPassing','BallControl',
               'Acceleration','Sprint Speed','Agility','Reactions','Balance','Shot Power',
               'Jumping','Stamina','Strength','Long Shots','Aggression','Interceptions',
               'Positioning','Vision','Penalties','Composure','Marking','Standing Tackle',
               'Sliding Tackle', 'Goalkeeper Diving', 'Goalkeeper Handling',
               'Goalkeeper Kicking', 'Goalkeeper Positioning', 'Goalkeeper Reflexes']

# Grafico varianza spiegata
def grafico_vs(vs):
    # Grafico varianza spiegata
    plt.figure(figsize=(8, 6))
    plt.bar(range(1, len(vs) + 1), vs, align='center')
    plt.title('Varianza spiegata per componente')
    plt.xlabel('Componenti')
    plt.ylabel('Varianza spiegata')
    plt.xticks(range(1, len(vs) + 1), attribute_names, rotation=90)
    plt.show()

# Grafico varianza spiegata cumulativa
def grafico_vsc(vsc):
    plt.figure(figsize=(8, 6))
    plt.plot(range(1, len(vsc) + 1), vsc, marker='o', linestyle='-', color='b')
    plt.title('Varianza cumulativa spiegata')
    plt.xlabel('Numero di componenti principali')
    plt.ylabel('Varianza cumulativa spiegata')
    plt.xticks(range(1, len(vsc) + 1), attribute_names, rotation=90)
    plt.axhline(y=0.95, color='r', linestyle='--', label='90% Varianza Spiegata')
    plt.show()