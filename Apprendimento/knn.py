from sklearn.neighbors import KNeighborsRegressor
import apprendimento as ap
import creazione_grafici as cg

def knn(training_x, training_y, test_x, test_y):
    medie_training = [] # array per conservare le medie sul training set
    medie_test = [] # array per conservare le medie sul test set
    rmse_training = []
    lista_k = [5, 7, 10, 15, 20, 30, 50] # numeri di vicini da valutare

    # valutazione del modello alle diverse profondita
    for k in lista_k:
        # definizione del modello
        modello = KNeighborsRegressor(n_neighbors=k)

        # calcolo dell'rmse sugli esempi di training
        modello, rmse = ap.train(modello, training_x, training_y)
        rmse_training.append(rmse)
        print("RMSE con numero di vicini = {}: ".format(k),rmse)

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
    cg.grafico_knn(lista_k, rmse_training, medie_training, medie_test)