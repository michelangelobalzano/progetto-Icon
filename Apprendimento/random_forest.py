from sklearn.ensemble import RandomForestRegressor
import apprendimento as ap
import creazione_grafici as cg

MAX_FEATURES = 8

######################################################################################################################
# Metodo che restituisce il miglior numero di alberi per il random forest
def n_alberi(training_x, training_y, test_x, test_y):

    rmse_training = []
    medie_training = [] # array per conservare le medie sul training set
    medie_test = [] # array per conservare le medie sul test set
    lista_n_alberi = [5, 10, 15, 20, 25, 30] # numeri di alberi da valutare
    # valutazione del modello con numeri di alberi diversi
    for n in lista_n_alberi:
        # definizione del modello
        modello = RandomForestRegressor(n_estimators=n, max_features=MAX_FEATURES)

        # calcolo dell'rmse sugli esempi di training
        modello, rmse = ap.train(modello, training_x, training_y)
        rmse_training.append(rmse)
        print("RMSE con numero di alberi = {}: ".format(n),rmse)

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
    cg.grafico_rf_n_alberi(lista_n_alberi, rmse_training, medie_training, medie_test)

    # restituzione del numero di alberi corrispondente al risultato minimo del test
    return lista_n_alberi[medie_test.index(min(medie_test))]

######################################################################################################################
# Algoritmo random forest
def random_forest(training_x, training_y, test_x, test_y):

    rmse_training = []
    medie_training = [] # array per conservare le medie sul training set
    medie_test = [] # array per conservare le medie sul test set
    lista_profondita = [5, 10, 15, 20, 25, 30] # profondita massime da valutare

    n = n_alberi(training_x, training_y, test_x, test_y)
    print("Numero di alberi migliore: ", n)

    # valutazione del modello alle diverse profondita
    for p in lista_profondita:
        # definizione del modello
        modello = RandomForestRegressor(n_estimators=n, max_depth=p, max_features=MAX_FEATURES)

        # calcolo dell'rmse sugli esempi di training
        modello, rmse = ap.train(modello, training_x, training_y)
        rmse_training.append(rmse)
        print("RMSE a profondita' {}: ".format(p),rmse)

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
    cg.grafico_rf_profondita(lista_profondita, rmse_training, medie_training, medie_test)