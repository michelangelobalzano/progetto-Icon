import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error

CROSS_VALIDATION = 10 # numero di fold per la k-fold cross validation

def train(modello, x, y):
    modello.fit(x, y)
    predizioni = modello.predict(x)
    mse = mean_squared_error(y, predizioni)
    rmse = round(np.sqrt(mse), 2)
    return modello, rmse

def k_fold(modello, x, y):
    punteggi_mse = -cross_val_score(modello, x, y, scoring='neg_mean_squared_error', cv=CROSS_VALIDATION)
    punteggi_rmse = np.around(np.sqrt(punteggi_mse), 2)
    media = round(punteggi_rmse.mean(), 2)
    return modello, media

def test(modello, x, y):
    predizioni = modello.predict(x)
    mse = mean_squared_error(y, predizioni)
    rmse = round(np.sqrt(mse), 2)
    return modello, rmse