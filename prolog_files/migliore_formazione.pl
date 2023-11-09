% ricerca del miglior giocatore per ruolo
miglior_calciatore(Posizione, Nome) :- calciatore(Nome, Posizione, Overall),
    \+ (calciatore(_, Posizione, AltroOverall), AltroOverall > Overall).

% ricerca della miglior formazione per modulo
formazione(Modulo, Calciatori) :- 
    modulo(Modulo, Ruoli),
    seleziona_calciatori_senza_duplicati(Ruoli, [], Calciatori).

% Nuova regola per selezionare calciatori senza duplicati
seleziona_calciatori_senza_duplicati([], _, []).
seleziona_calciatori_senza_duplicati([Ruolo | AltriRuoli], Selezionati, [Calciatore | AltriCalciatori]) :-
    miglior_calciatore_senza_duplicati(Ruolo, Selezionati, Calciatore),
    seleziona_calciatori_senza_duplicati(AltriRuoli, [Calciatore | Selezionati], AltriCalciatori).

% Definizione di miglior_calciatore_senza_duplicati/3
miglior_calciatore_senza_duplicati(Ruolo, Selezionati, Calciatore) :-
    calciatore(Calciatore, Ruolo, Overall),
    \+ member(Calciatore, Selezionati),  % Assicurati che il calciatore non sia già stato selezionato
    calciatore_migliore_senza_duplicati(Ruolo, Overall, Selezionati, Calciatore).

% Definizione di calciatore_migliore_senza_duplicati/4
calciatore_migliore_senza_duplicati(Ruolo, Overall, Selezionati, MiglioreCalciatore) :-
    calciatore(AltroCalciatore, Ruolo, AltroOverall),
    AltroOverall =< Overall,  % Verifica che l altro calciatore abbia un overall inferiore o uguale
    \+ member(AltroCalciatore, Selezionati),  % Assicurati che l altro calciatore non sia stato selezionato
    migliore_overall_senza_duplicati(Ruolo, AltroOverall, Selezionati, MiglioreCalciatore).

% Definizione di migliore_overall_senza_duplicati/4
migliore_overall_senza_duplicati(Ruolo, AltroOverall, _, AltroCalciatore) :-
    calciatore(AltroCalciatore, Ruolo, AltroOverall).
migliore_overall_senza_duplicati(Ruolo, AltroOverall, Selezionati, MiglioreCalciatore) :-
    calciatore_migliore_senza_duplicati(Ruolo, AltroOverall, Selezionati, MiglioreCalciatore).

% moduli
modulo(433, [gk, lb, cb, cb, rb, cdm, cm, cm, lw, rw, st]).
modulo(352, [gk, cb, cb, cb, lm, cm, cdm, cm, rm, st, st]).
modulo(4231, [gk, lb, cb, cb, rb, cdm, cdm, lw, cam, rw, st]).
modulo(442, [gk, lb, cb, cb, rb, lm, cm, cm, rm, st, st]).