from CSP.libs.cspProblems import Variable, Constraint, CSP
from CSP.libs.cspSLS import SLSearcher

def turno_infrasettimanale(numero):
    if numero == 4 or numero == 14 or numero == 16 or numero == 33:
        return True
    else:
        return False

def derby(casa, ospite):
    if casa == "inter" and ospite == "milan":
        return True
    elif casa == "milan" and ospite == "inter":
        return True
    elif casa == "juve" and ospite == "torino":
        return True
    elif casa == "torino" and ospite == "juve":
        return True
    elif casa == "napoli" and ospite == "salernitana":
        return True
    elif casa == "salernitana" and ospite == "napoli":
        return True
    elif casa == "fiorentina" and ospite == "empoli":
        return True
    elif casa == "empoli" and ospite == "fiorentina":
        return True
    elif casa == "roma" and ospite == "lazio":
        return True
    elif casa == "lazio" and ospite == "roma":
        return True
    else:
        return False
    
def importante(squadra):
    if squadra == "inter":
        return True
    elif squadra == "milan":
        return True
    elif squadra == "lazio":
        return True
    elif squadra == "roma":
        return True
    elif squadra == "juventus":
        return True
    elif squadra == "napoli":
        return True
    elif squadra == "fiorentina":
        return True
    else:
        return False
    
Casa = Variable ("Casa", {"atalanta", "bologna", "cremonese", "empoli", "fiorentina", "hellas_verona", 
                          "inter", "juventus", "lazio", "lecce", "milan", "monza", "napoli", "roma", 
                          "salernitana", "sampdoria", "sassuolo", "spezia", "torino", "udinese"})

Ospite = Variable ("Casa", {"atalanta", "bologna", "cremonese", "empoli", "fiorentina", "hellas_verona", 
                          "inter", "juventus", "lazio", "lecce", "milan", "monza", "napoli", "roma", 
                          "salernitana", "sampdoria", "sassuolo", "spezia", "torino", "udinese"})

Giornata = Variable ("Giornata", {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 
                                                18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 
                                                33, 34, 35, 36, 37, 38})

C0 = Constraint ([Giornata, Casa, Ospite], not(derby(Casa, Ospite)) and not(turno_infrasettimanale(Giornata)), "No derby in turni infrasettimanali")

C1 = Constraint ([Giornata, Casa, Ospite], not(importante(Casa) and importante(Ospite)) and not (turno_infrasettimanale(Giornata)), "No partite importanti in turni infrasettimanali")

C2 = Constraint ([Giornata, Casa, Ospite], not(Giornata == 1 and derby(Casa, Ospite)), "No derby alla prima giornata")