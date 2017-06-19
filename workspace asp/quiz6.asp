% Luke S. Hart
% CSE 471: Intro to AI
% Zebra Quiz

% Define the possible values for the appropriate fields
housePosition(1..5). % 1st house is the leftmost house
colors(red;green;ivory;yellow;blue). % colors of the houses
drinks(coffee;tea;milk;oj;water). % types of drinks
nations(england;spain;ukraine;norway;japan). % different nations the women came from
pets(dog;snail;fox;horse;zebra). % types of pets the women have
jobs(engineer;diplomat;doctor;teacher;carpenter). % types of jobs the women have

% Generate all possible combinations
1 { isColor(H,C) : colors(C) } 1 :- housePosition(H).
1 { isColor(H,C) : housePosition(H) } 1 :- colors(C).

1 { ownerLikes(H,D) : drinks(D) } 1 :- housePosition(H).
1 { ownerLikes(H,D) : housePosition(H) } 1 :- drinks(D).

1 { isFrom(H,N) : nations(N) } 1 :- housePosition(H).
1 { isFrom(H,N) : housePosition(H) } 1 :- nations(N).

1 { ownsPet(H,P) : pets(P) } 1 :- housePosition(H).
1 { ownsPet(H,P) : housePosition(H) } 1 :- pets(P).

1 { worksAs(H,J) : jobs(J) } 1 :- housePosition(H).
1 { worksAs(H,J) : housePosition(H) } 1 :- jobs(J).

% All those clues, listed in order
clue1 :- housePosition(H), isFrom(H,england), isColor(H,red).
:- not clue1.

clue2 :- housePosition(H), isFrom(H,spain), ownsPet(H,dog).
:- not clue2.

clue3 :- housePosition(H), ownerLikes(H,coffee), isColor(H,green).
:- not clue3.

clue4 :- housePosition(H), isFrom(H,ukraine), ownerLikes(H,tea).
:- not clue4.

clue5 :- housePosition(H), isColor(H,ivory), isColor(H+1,green), H < 5.
:- not clue5.

clue6 :- housePosition(H), worksAs(H,engineer), ownsPet(H,snail).
:- not clue6.

clue7 :- housePosition(H), worksAs(H,diplomat), isColor(H,yellow).
:- not clue7.

clue8 :- ownerLikes(3,milk).
:- not clue8.

clue9 :- isFrom(1,norway).
:- not clue9.

clue10 :- housePosition(H), housePosition(H2),
 worksAs(H,doctor), ownsPet(H2,fox), |H - H2| = 1.
:- not clue10.

clue11 :- housePosition(H), housePosition(H2),
 worksAs(H,diplomat), ownsPet(H2,horse), |H - H2| = 1.
:- not clue11.

clue12 :- housePosition(H), worksAs(H,teacher), ownerLikes(H,oj).
:- not clue12.

clue13 :- housePosition(H), isFrom(H,japan), worksAs(H,carpenter).
:- not clue13.

clue14 :- housePosition(H), housePosition(H2),
 isFrom(H,norway), isColor(H2,blue), |H - H2| = 1.
:- not clue14.

% Display answer
drinksWater(N) :- housePosition(H), isFrom(H,N), ownerLikes(H,water).
ownsZebra(N) :- housePosition(H), isFrom(H,N), ownsPet(H,zebra).
#show drinksWater/1.
#show ownsZebra/1.
