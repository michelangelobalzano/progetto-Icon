% mappatura dei reparti
reparto(portiere, 'gk').
reparto(difensore, 'lb').
reparto(difensore, 'rb').
reparto(difensore, 'cb').
reparto(difensore, 'rwb').
reparto(difensore, 'lwb').
reparto(centrocampista, 'cm').
reparto(centrocampista, 'cdm').
reparto(centrocampista, 'rm').
reparto(centrocampista, 'lm').
reparto(centrocampista, 'cam').
reparto(attaccante, 'cf').
reparto(attaccante, 'rf').
reparto(attaccante, 'lf').
reparto(attaccante, 'rw').
reparto(attaccante, 'lw').
reparto(attaccante, 'st').

% disponibilità di un numero per una squadra
numero_disponibile(Squadra, Numero) :-
    squadra(_, Squadra),
    \+ numero(_, Numero).

% Verifica se due calciatori giocano nello stesso reparto
stesso_reparto(GiocatoreA, GiocatoreB) :-
    ruolo(GiocatoreA, RuoloA),
    ruolo(GiocatoreB, RuoloB),
    reparto(Reparto, RuoloA),
    reparto(Reparto, RuoloB).

% Verifica se due calciatori giocano nella stessa squadra
compagni_di_squadra(GiocatoreA, GiocatoreB) :-
    squadra(GiocatoreA, Squadra),
    squadra(GiocatoreB, Squadra).

% Verifica se due calciatori giocano nella stessa nazionale
compagni_in_nazionale(GiocatoreA, GiocatoreB) :-
    nazionalita(GiocatoreA, Nazionale),
    nazionalita(GiocatoreB, Nazionale).

% Verifica se il calciatore è il migliore per la sua squadra
miglior_giocatore_squadra(Calciatore) :-
    squadra(Calciatore, Squadra),
    overall(Calciatore, Overall),
    \+ (squadra(GiocatoreB, Squadra), overall(GiocatoreB, OverallB), OverallB > Overall).

% Verifica se il calciatore è il migiore per la sua squadra nel suo reparto
miglior_giocatore_squadra_reparto(Calciatore) :-
    squadra(Calciatore, Squadra),
    overall(Calciatore, Overall),
    \+ (squadra(GiocatoreB, Squadra),
        overall(GiocatoreB, OverallB),
        stesso_reparto(Calciatore, GiocatoreB),
        OverallB > Overall).

% Verifica se il contratto del calciatore scade nell anno corrente
contratto_in_scadenza(Calciatore) :- 
    scadenza(Calciatore, Scadenza),
    Scadenza = 2023.

% Verifica se il calciatore è una bandiera per la propria squadra
% Considerando bandiera un calciatore che gioca per la propria squadra da almeno 10 anni
bandiera(Calciatore) :-
    inizio(Calciatore, Inizio),
    Risultato is 2023 - Inizio,
    integer(Risultato),
    Risultato >= 10.
    
% Verifica se due calciatori hanno lo stesso piede preferito
stesso_piede(GiocatoreA, GiocatoreB) :-
    piede(GiocatoreA, PiedeA),
    piede(GiocatoreB, PiedeB),
    PiedeA = PiedeB.

% Verifica se il calciatore ha margine di in_crescita
% Un calciatore ha margine di crescita se ha un potenziale maggiore dell overall
in_crescita(Calciatore) :-
    overall(Calciatore, Overall),
    potenziale(Calciatore, Potenziale),
    Potenziale > Overall.

% Verifica se i due calciatori giocano nella stessa squadra e nella stessa nazionale
doppiamente_compagni(GiocatoreA, GiocatoreB) :-
    compagni_di_squadra(GiocatoreA, GiocatoreB),
    compagni_in_nazionale(GiocatoreA, GiocatoreB).