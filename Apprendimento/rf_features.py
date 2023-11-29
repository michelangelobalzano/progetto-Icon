from sklearn.ensemble import RandomForestRegressor
import apprendimento as ap
import matplotlib.pyplot as plt
from preprocessing import preprocessing

N_ESTIMATORS = 25
MAX_DEPTH = 20

training_x, training_y, test_x, test_y = preprocessing()
rmse_training = []
medie_training = [] # array per conservare le medie sul training set
medie_test = [] # array per conservare le medie sul test set
lista_features = [5, 10, 15, 20, 25, 30] # features massime da valutare

# valutazione del modello alle diverse profondita
for f in lista_features:
    # definizione del modello
    modello = RandomForestRegressor(n_estimators=N_ESTIMATORS, max_depth=MAX_DEPTH, max_features=f)

    # calcolo dell'rmse sugli esempi di training
    modello, rmse = ap.train(modello, training_x, training_y)
    rmse_training.append(rmse)
    print("RMSE max features = {}: ".format(f),rmse)

    # calcolo degli rmse con la k-fold cross validation sugli esempi di training
    modello, media = ap.k_fold(modello, training_x, training_y)
    medie_training.append(media)

    # calcolo dell'rmse sugli esempi di test
    modello, rmse_finale = ap.test(modello, test_x, test_y)
    medie_test.append(rmse_finale)

# stampa dei risultati
print("Medie training: ", medie_training)
print("Medie test: ", medie_test)

# creazione del grafico dei risultati
plt.figure(figsize=(10, 6))
plt.plot(lista_features, rmse, label='Train RMSE')
plt.plot(lista_features, medie_training, label='K-Fold RMSE')
plt.plot(lista_features, medie_test, label='Test RMSE')
plt.xlabel("F (numero di features massimo)")
plt.ylabel('RMSE (Root Mean Squared Error)')
plt.legend()
plt.title("Random forest al variare di F")
plt.savefig("Apprendimento/grafici/rf_features.png")
plt.show()