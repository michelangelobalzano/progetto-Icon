from preprocessing import preprocessing
import regressione_lineare as rl
import albero_decisionale as ad
import knn
import random_forest as rf

# preparazione dei dati di training e set
training_x, training_y, test_x, test_y = preprocessing()
    
print("1: regressione lineare")
print("2: alberi decisionali")
print("3: knn")
print("4: random forest")

while True:
    while True:
        scelta = int(input("Digitare scelta: "))

        if(scelta >= 1 and scelta <= 4):
            break
        else:
            print("Input non valido")

    if (scelta == 1):
        rl.regressione_lineare(training_x, training_y, test_x, test_y)
    elif (scelta == 2):
        ad.albero_decisionale(training_x, training_y, test_x, test_y)
    elif (scelta == 3):
        knn.knn(training_x, training_y, test_x, test_y)
    elif (scelta == 4):
        rf.random_forest(training_x, training_y, test_x, test_y)

    uscita = int(input("Digitare 0 per ripetere con un altro modello: "))

    if (uscita != 0):
        break