import matplotlib.pyplot as plt

######################################################################################################################
# Stampa grafico regressione lineare
def grafico_rl(rmse, media, rmse_finale):
    labels = ['Train RMSE', 'K-fold RMSE', 'Test RMSE']
    heights = [rmse, media, rmse_finale]
    plt.bar(labels, heights, color=['tab:blue', 'tab:orange', 'tab:green'])
    plt.ylabel('RMSE (Root Mean Squared Error)')
    plt.title('Regressione lineare')
    plt.savefig("Apprendimento/grafici/rl.png")
    plt.show()

######################################################################################################################
# Stampa grafico albero decisionale
def grafico_ad(lista_profondita, rmse_training, medie_training, medie_test):
    plt.figure(figsize=(10, 6))
    plt.plot(lista_profondita, rmse_training, label='Train RMSE')
    plt.plot(lista_profondita, medie_training, label='K-fold RMSE')
    plt.plot(lista_profondita, medie_test, label='Test RMSE')
    plt.xlabel("P (Profondita' massima alberi)")
    plt.ylabel('RMSE (Root Mean Squared Error)')
    plt.legend()
    plt.title("Albero decisionale al variare di P")
    plt.savefig("Apprendimento/grafici/ad.png")
    plt.show()

######################################################################################################################
# Stampa grafico knn
def grafico_knn(lista_k, rmse, medie_training, medie_test):
    plt.figure(figsize=(10, 6))
    plt.plot(lista_k, rmse, label='Train RMSE')
    plt.plot(lista_k, medie_training, label='K-fold RMSE')
    plt.plot(lista_k, medie_test, label='Test RMSE')
    plt.xlabel("K (Numero di vicini)")
    plt.ylabel('RMSE (Root Mean Squared Error)')
    plt.legend()
    plt.title("KNN al variare di K")
    plt.savefig("Apprendimento/grafici/knn.png")
    plt.show()

######################################################################################################################
# Stampa grafico random forest al variare del numero di alberi
def grafico_rf_n_alberi(lista_n_alberi, rmse, medie_training, medie_test):
    plt.figure(figsize=(10, 6))
    plt.plot(lista_n_alberi, rmse, label='Train RMSE')
    plt.plot(lista_n_alberi, medie_training, label='Training RMSE')
    plt.plot(lista_n_alberi, medie_test, label='Test RMSE')
    plt.xlabel("N (numero di alberi)")
    plt.ylabel('RMSE (Root Mean Squared Error)')
    plt.legend()
    plt.title("Random forest al variare di N")
    plt.savefig("Apprendimento/grafici/rf_n_alberi.png")
    plt.show()

######################################################################################################################
# Stampa grafico random forest al variare della profondita massima
def grafico_rf_profondita(lista_profondita, rmse, medie_training, medie_test):
    plt.figure(figsize=(10, 6))
    plt.plot(lista_profondita, rmse, label='Train RMSE')
    plt.plot(lista_profondita, medie_training, label='Training RMSE')
    plt.plot(lista_profondita, medie_test, label='Test RMSE')
    plt.xlabel("P (Profondita' massima alberi)")
    plt.ylabel('RMSE (Root Mean Squared Error)')
    plt.legend()
    plt.title("Random forest al variare di P")
    plt.savefig("Apprendimento/grafici/rf_profondita.png")
    plt.show()
