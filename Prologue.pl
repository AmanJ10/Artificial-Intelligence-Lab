male(ram).
male(lakshman).
male(bharat).
male(shatrughna).
male(dasharatha).
male(kush).
male(luv).

female(sita).
female(kaushalya).

parent(dasharatha, ram).
parent(dasharatha, bharat).
parent(dasharatha, lakshman).
parent(dasharatha, shatrughna).
parent(kaushalya, ram).
parent(kaushalya, bharat).
parent(kaushalya, lakshman).
parent(kaushalya, shatrughna).
parent(ram, luv).
parent(sita, luv).
parent(ram, kush).
parent(sita, kush).

wife(kaushalya, dasharatha).
wife(sita, ram).

brother(X, Y) :-
    male(X),
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

uncle(X, Y) :-
    parent(Z, X),
    parent(Z, W),
    parent(W, Y),
    male(X),
    X \= W.

step_mother(X, Y) :-
    parent(Z, Y),
    parent(Z, W),
    wife(X, Z),
    female(X).

grandparent(X, Y) :-
    parent(X, W),
    parent(W, Y).

mother_in_law(X, Y) :-
    wife(Y, Z),
    parent(X, Z),
    female(X),
    female(Y),
    male(Z).

brother_in_law(X, Y) :-
   female(Y),
   wife(Y, Z),
   brother(X, Z).
