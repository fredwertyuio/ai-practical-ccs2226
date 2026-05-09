parent(john,mary).
parent(john,peter).
parent(mary,alice).

male(john).
female(mary).

father(X,Y):-parent(X,Y),male(X).
mother(X,Y):-parent(X,Y),female(X).

grandparent(X,Y):-parent(X,Z),parent(Z,Y).