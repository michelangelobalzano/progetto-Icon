from main_manager import *

while True:
    clearConsole()
    print("CALCOLO MIGLIORE FORMAZIONE CON BUDGET\n")
    print("1 = Effettuare un singolo calcolo")
    print("2 = Testare un algoritmo")
    print("3 = Confrontare gli algoritmi")

    while True:
        scelta = int(input("Inserire scelta: "))
        if(scelta >= 1 and scelta <= 3):
            break
        else:
            print("Scelta non valida!")

    if (scelta == 1):
        calcolo_singolo()
    elif (scelta == 2):
        test_algoritmi()
    elif (scelta == 3):
        confronto_algoritmi()

    uscita = int(input("Digitare 0 per ripetere: "))

    if (uscita != 0):
        break