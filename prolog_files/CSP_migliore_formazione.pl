% regola principale: prende un modulo in input e restituisce la lista dei calciatori migliori per ogni ruolo del modulo
migliore_formazione(Modulo, Calciatori) :-
    % ottenimento della lista dei ruoli del modulo in input 
    modulo(Modulo, Ruoli),
    % selezione del miglior calciatore per ogni ruolo
    seleziona_calciatori_senza_duplicati(Ruoli, [], Calciatori).

% regola ricorsiva per cercare i calciatori senza duplicati
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