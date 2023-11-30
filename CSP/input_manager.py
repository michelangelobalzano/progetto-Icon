######################################################################################################################
# Metodo per prendere in input un modulo valido
def input_modulo():
    
    print("Moduli disponibili: 433, 442, 4231, 352")
    while True:
        scelta = int(input("Inserire modulo: "))

        if(scelta == 433 or scelta == 4231 or scelta == 442 or scelta == 352):
            break
        else:
            print("Modulo non valido!")
    if scelta == 433:
        modulo = ['Portiere', 'Terzino sinistro', 'Difensore centrale', 'Difensore centrale', 
                  'Terzino destro', 'Centrocampista centrale', 'Mediano', 'Centrocampista centrale', 
                  'Ala sinistra', 'Prima punta', 'Ala destra']
    elif scelta == 4231:
        modulo = ['Portiere', 'Terzino sinistro', 'Difensore centrale', 'Difensore centrale', 
                  'Terzino destro', 'Mediano', 'Mediano', 'Ala sinistra', 'Trequartista', 
                  'Ala destra', 'Prima punta']
    elif scelta == 442:
        modulo = ['Portiere', 'Terzino sinistro', 'Difensore centrale', 'Difensore centrale', 
                  'Terzino destro', 'Esterno sinistro', 'Centrocampista centrale', 'Centrocampista centrale', 
                  'Esterno destro', 'Prima punta', 'Prima punta']
    elif scelta == 352:
        modulo = ['Portiere', 'Difensore centrale', 'Difensore centrale', 'Difensore centrale', 
                  'Esterno sinistro', 'Centrocampista centrale', 'Mediano', 'Centrocampista centrale', 
                  'Esterno destro', 'Prima punta', 'Prima punta']

    return modulo

######################################################################################################################
# Metodo per prendere in input un budget valido
def input_budget():

    print("Budget minimo: 300 (milioni)")
    print("Budget massimo: 500 (milioni)")
    while True:
        budget = int(input("Inserire budget: "))

        if(budget >= 300 and budget <= 500):
            break
        else:
            print("Budget non valido")
    return budget