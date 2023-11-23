import pandas as pd
from pyswip import Prolog
from preprocessing import preprocessing

# calcolo della migliore formazione
def trova_migliore_formazione(modulo):
    
    # formulazione della query
    formazione_query = 'migliore_formazione({}, Calciatori).'.format(modulo)
    
    migliori_calciatori = []
    for risultato in prolog.query(formazione_query):
        calciatori = risultato['Calciatori']
        for calciatore in calciatori:
            migliori_calciatori.append(str(calciatore))
        return migliori_calciatori
    
    else:
        print("nessuna formazione trovata!")

    return 

def ruoli_modulo(modulo):
    ruoli_modulo = []
    for risultato in prolog.query("modulo({}, Ruoli)".format(modulo)):
        ruoli = risultato['Ruoli']
        for ruolo in ruoli:
            ruoli_modulo.append(str(ruolo))

    return ruoli_modulo

while True:
    while True:
        # input della nazionalita
        nazionalita = input("Inserire nome dello stato in inglese oppure 'all' per scegliere tutto il mondo: ")

        # creazione del dataset
        i = preprocessing(nazionalita)
        if (i == 0):
            print ("nazionalita' non valida!")
        else:
            break
        
    # caricamento dei file prolog
    prolog = Prolog()
    prolog.consult("prolog_files/CSP_migliore_formazione.pl")
    prolog.consult("prolog_files/kb_calciatori_CSP.pl")

    # input del modulo
    modulo = input("Inserire modulo (433, 352, 4231, 442): ")

    # ricerca dei ruoli del modulo
    ruoli = ruoli_modulo(modulo)

    # calcolo della migliore formazione
    migliori_calciatori = trova_migliore_formazione(modulo)

    for i in range (11):
        print(ruoli[i], ": ", migliori_calciatori[i])

    uscita = int(input("Digitare 0 per ripetere con un altra nazionale: "))

    if (uscita != 0):
        break