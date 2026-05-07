% =====================================================
% PROGRAMA PROLOG: RELAÇÕES FAMILIARES
% =====================================================
% Exemplo introdutório para demonstrar conceitos
% básicos de programação lógica em Prolog

% =====================================================
% FATOS: Informações básicas sobre a família
% =====================================================

% Fatos de parentesco - pai
pai(carlos, joao).
pai(carlos, maria).
pai(joao, ana).
pai(joao, pedro).
pai(luis, carlos).

% Fatos de parentesco - mãe
mae(teresa, joao).
mae(teresa, maria).
mae(sofia, ana).
mae(sofia, pedro).

% =====================================================
% REGRAS: Relações derivadas a partir dos fatos
% =====================================================

% Regra 1: Alguém é filho se é filho do pai OU da mãe
filho(X, Y) :- pai(Y, X).
filho(X, Y) :- mae(Y, X).

% Regra 2: Alguém é avô/avó se é pai/mãe do pai/mãe
avo(X, Z) :- pai(X, Y), pai(Y, Z).
avo(X, Z) :- pai(X, Y), mae(Y, Z).
avo(X, Z) :- mae(X, Y), pai(Y, Z).
avo(X, Z) :- mae(X, Y), mae(Y, Z).

% Regra 3: Alguém é irmão/irmã se compartilha o mesmo pai ou mãe
irmao(X, Y) :- pai(P, X), pai(P, Y), X \= Y.
irmao(X, Y) :- mae(M, X), mae(M, Y), X \= Y.

% =====================================================
% CONSULTAS DEMONSTRADAS
% =====================================================

% Consulta 1: Quem é filho de carlos?
% Resposta esperada: joao, maria
% ?- filho(X, carlos).

% Consulta 2: Quem é avô de ana?
% Resposta esperada: luis
% Esta consulta depende de REGRA (avo), não de um fato direto
% ?- avo(X, ana).

% Consulta 3: Quem é irmão de joao?
% Resposta esperada: maria
% ?- irmao(joao, X).
