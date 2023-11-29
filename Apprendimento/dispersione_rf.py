import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from preprocessing import preprocessing
import apprendimento as ap

######################################################################################################################
# migliori valori degli iperparametri
N_ESTIMATORS = 25
MAX_DEPTH = 20
MAX_FEATURES = 8

######################################################################################################################
# Creazione grafico di dispersione random forest

training_x, training_y, test_x, test_y = preprocessing()

# definizione del modello
modello = RandomForestRegressor(n_estimators=N_ESTIMATORS, max_depth=MAX_DEPTH, max_features=MAX_FEATURES)

# calcolo dell'rmse sugli esempi di training
modello, rmse = ap.train(modello, training_x, training_y)

# calcolo degli rmse con la k-fold cross validation sugli esempi di training
modello, media = ap.k_fold(modello, training_x, training_y)

# selezione dei primi 100 esempi
esempi = test_x.iloc[:100]
target = test_y.iloc[:100]

# calcolo delle predizioni
predizioni = modello.predict(esempi)

# creazione grafico di dispersione
plt.scatter(target, predizioni, color='tab:blue')
plt.plot([min(target), max(target)], [min(target), max(target)], linestyle='--', color='tab:orange', linewidth=2)
plt.xlabel('Valori Attesi')
plt.ylabel('Predizioni del Modello')
plt.title('Confronto tra Predizioni e Valori Attesi su 100 Esempi')
plt.savefig("Apprendimento/grafici/dispersione_rf.png")
plt.show()