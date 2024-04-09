parent(kaushalya,ram).
parent(dasharat,ram).
parent(dasharat, lakshman).
parent(dasharat, bharat).
parent(dasharat, shatrughna).
male(dasharat).
male(ram).
male(lakshman).
male(bharat).
male(shatrughna).
female(sita).
female(kaushalya).
wife(sita,ram).
wife(kaushalya,dasharat).
father_in_law(X, Y) :- father(X, Z), wife(Y, Z).
mother_in_law(X, Y) :- mother(X, Z), wife(Y, Z).
father(X,Y):- parent(X,Y),male(X).
mother(X,Y):-parent(X,Y),female(X).
brother_in_law(X,Y):- wife(Y,Z),parent(K,Z),parent(K,X).
