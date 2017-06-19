% Luke S. Hart
% CSE 471: Intro to AI
% Project 4: Puzzle 2

% Define the possible values for the appropriate fields
years(2007; 2008; 2009; 2010).
supers(bane; shadow; hex; wonder). % Criminal Bane, Deep Shadow, Ultra Hex, Wonderman
names(gabe; ivor; matt; peter). % Gabe Grant, Ivor Ingram, Matt Minkle, Peter Powers

% Generate all possible combinations
1 {isSuper(N,S): supers(S)} 1 :- names(N).
1 {startedIn(N,Y): years(Y) } 1 :- names(N).

% Remove combinations with duplicate supers or starting years
:- names(N), names(N2), supers(S), isSuper(N,S), isSuper(N2, S), N != N2.
:- names(N), names(N2), years(Y), startedIn(N,Y), startedIn(N2, Y), N != N2.

% Ultra Hex is Gabe
isSuper(gabe, hex).

% Bane started in either 2007 or 2009, so I explicitly removed 2008 and 2010
% (because I couldn't figure out how to do it smarted than that)
:- names(N), isSuper(N, bane), startedIn(N,2008).
:- names(N), isSuper(N, bane), startedIn(N,2010).

% Peter began before Matt
:- startedIn(peter, Y), startedIn(matt, Y2), Y2 < Y.

% Gabe started 1 year after Wonderman
:- names(N), years(Y), startedIn(gabe, Y2), isSuper(N, wonder),
startedIn(N,Y), Y2 != Y+1.

% Basically capturing the restrictions implicit in clue #5
% (Deep Shadow isn't matt and didn't start in 2007 or 2009, etc)
:- names(N), isSuper(N, shadow), startedIn(N, 2007).
:- names(N), isSuper(N, shadow), startedIn(N, 2009).
:- isSuper(matt, shadow).
:- startedIn(matt, 2007).
:- startedIn(matt, 2009).

% Display
nameSuperYear (N,S,Y):- isSuper(N,S), startedIn(N,Y).
#show nameSuperYear/3.
