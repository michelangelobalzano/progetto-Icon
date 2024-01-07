from pyswip import Prolog

# Inizializza l'interprete Prolog
prolog = Prolog()

# Carica i file prolog
prolog.consult("prolog_files/kb_fatti.pl")
prolog.consult("prolog_files/kb_regole.pl")

print("NUMERO DISPONIBILE")

# Formula una query
query = "numero_disponibile(liverpool, 67)"  # Esempio di query
# Stampare i risultati
result = list(prolog.query(query))
print(query)
print(bool(result))

# Formula una query
query = "numero_disponibile(liverpool, 11)"  # Esempio di query
# Stampare i risultati
result = list(prolog.query(query))
print(query)
print(bool(result), "\n")

print("STESSO REPARTO")

# Formula una query
query = "stesso_reparto(k_mbappe, r_lewandowski)"  # Esempio di query
# Stampare i risultati
result = list(prolog.query(query))
print(query)
print(bool(result))

# Formula una query
query = "stesso_reparto(k_mbappe, t_courtois)"  # Esempio di query
# Stampare i risultati
result = list(prolog.query(query))
print(query)
print(bool(result), "\n")

print("COMPAGNI DI SQUADRA")

# Formula una query
query = "compagni_di_squadra(v_van_dijk, m_salah)"  # Esempio di query
# Stampare i risultati
result = list(prolog.query(query))
print(query)
print(bool(result))

# Formula una query
query = "compagni_di_squadra(k_mbappe, m_salah)"  # Esempio di query
# Stampare i risultati
result = list(prolog.query(query))
print(query)
print(bool(result), "\n")

print("COMPAGNI IN NAZIONALE")

# Formula una query
query = "compagni_in_nazionale(casemiro, neymar_jr)"  # Esempio di query
# Stampare i risultati
result = list(prolog.query(query))
print(query)
print(bool(result))

# Formula una query
query = "compagni_in_nazionale(k_mbappe, m_salah)"  # Esempio di query
# Stampare i risultati
result = list(prolog.query(query))
print(query)
print(bool(result), "\n")

print("MIGLIOR GIOCATORE SQUADRA")

# Formula una query
query = "miglior_giocatore_squadra(l_messi)"  # Esempio di query
# Stampare i risultati
result = list(prolog.query(query))
print(query)
print(bool(result))

# Formula una query
query = "miglior_giocatore_squadra(g_donnarumma)"  # Esempio di query
# Stampare i risultati
result = list(prolog.query(query))
print(query)
print(bool(result), "\n")

print("MIGLIOR GIOCATORE SQUADRA NEL REPARTO")

# Formula una query
query = "miglior_giocatore_squadra_reparto(marquinhos)"  # Esempio di query
# Stampare i risultati
result = list(prolog.query(query))
print(query)
print(bool(result))

# Formula una query
query = "miglior_giocatore_squadra_reparto(sergio_ramos)"  # Esempio di query
# Stampare i risultati
result = list(prolog.query(query))
print(query)
print(bool(result), "\n")

print("CONTRATTO IN SCADENZA")

# Formula una query
query = "contratto_in_scadenza(l_messi)"  # Esempio di query
# Stampare i risultati
result = list(prolog.query(query))
print(query)
print(bool(result))

# Formula una query
query = "contratto_in_scadenza(r_lewandowski)"  # Esempio di query
# Stampare i risultati
result = list(prolog.query(query))
print(query)
print(bool(result), "\n")

print("BANDIERA")

# Formula una query
query = "bandiera(k_benzema)"  # Esempio di query
# Stampare i risultati
result = list(prolog.query(query))
print(query)
print(bool(result))

# Formula una query
query = "bandiera(r_lewandowski)"  # Esempio di query
# Stampare i risultati
result = list(prolog.query(query))
print(query)
print(bool(result), "\n")

print("STESSO PIEDE")

# Formula una query
query = "stesso_piede(k_benzema, r_lewandowski)"  # Esempio di query
# Stampare i risultati
result = list(prolog.query(query))
print(query)
print(bool(result))

# Formula una query
query = "stesso_piede(l_messi, r_lewandowski)"  # Esempio di query
# Stampare i risultati
result = list(prolog.query(query))
print(query)
print(bool(result), "\n")

print("IN CRESCITA")

# Formula una query
query = "in_crescita(k_mbappe)"  # Esempio di query
# Stampare i risultati
result = list(prolog.query(query))
print(query)
print(bool(result))

# Formula una query
query = "in_crescita(l_messi)"  # Esempio di query
# Stampare i risultati
result = list(prolog.query(query))
print(query)
print(bool(result), "\n")

print("DOPPIAMENTE COMPAGNI")

# Formula una query
query = "doppiamente_compagni(k_mbappe, p_kimpembe)"  # Esempio di query
# Stampare i risultati
result = list(prolog.query(query))
print(query)
print(bool(result))

# Formula una query
query = "doppiamente_compagni(k_mbappe, l_messi)"  # Esempio di query
# Stampare i risultati
result = list(prolog.query(query))
print(query)
print(bool(result), "\n")