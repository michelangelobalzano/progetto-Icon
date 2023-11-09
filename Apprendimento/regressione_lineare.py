from sklearn.linear_model import LinearRegression
import apprendimento as ap
import creazione_grafici as cg

def regressione_lineare(training_x, training_y, test_x, test_y):
    # definizione del modello
    modello = LinearRegression()

    # calcolo dell'rmse sugli esempi di training
    modello, rmse = ap.train(modello, training_x, training_y)

    # calcolo degli rmse con la k-fold cross validation sugli esempi di training
    modello, media = ap.k_fold(modello, training_x, training_y)

    # calcolo dell'rmse sugli esempi di test
    modello, rmse_finale = ap.test(modello, test_x, test_y)

    # stampa dei risultati
    print("RMSE sul training set: ",rmse)
    print("Media ottenuta dopo la k-fold cross validation: ", media)
    print("RMSE sul test set: ", rmse_finale)

    cg.grafico_rl(rmse, media, rmse_finale)