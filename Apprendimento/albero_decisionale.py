from sklearn.tree import DecisionTreeRegressor
import apprendimento as ap
import creazione_grafici as cg

def albero_decisionale(training_x, training_y, test_x, test_y):
    rmse_training = []
    medie_training = [] # array per conservare le medie sul training set
    medie_test = [] # array per conservare le medie sul test set
    lista_profondita = [5, 10, 15, 20, 25, 30] # profondita massime da valutare

    # valutazione del modello alle diverse profondita
    for p in lista_profondita:
        # definizione del modello
        modello = DecisionTreeRegressor(max_depth=p)

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
    cg.grafico_ad(lista_profondita, rmse_training, medie_training, medie_test)