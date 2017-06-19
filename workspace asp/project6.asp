% Luke S. Hart
% CSE 471: Intro to AI
% Project 6

% Define the temporal scope of the problem (and a slightly narrower planning time, for simplicity)
time(1..8).
ptime(1..7).

% Define places entities can be and what entities can be where
positions(near; far).
entities(goat; cabbage; wolf; sailor).

% Define the things that can change in the world
fluent(on(E,P)) :- positions(P), entities(E).

% Define what actions can be taken
actions(move_sailor(P)) :- positions(P).
actions(move_something(E,P)) :- positions(P), entities(E), E != sailor.

% Define the initial conditions of the world.
initially(on(E, near)) :-  entities(E).

% Initialize the initial conditions
h(F,1) :- initially(F), fluent(F).

% Give states the property of inertia
h(F,T+1) :- h(F,T), not ab(F,T), fluent(F), time(T).

% Define how the actions change the world
% Action : move_sailor
h(on(sailor,P), T+1) :- o(move_sailor(P),T), time(T), positions(P), not h(on(sailor,P), T).
ab(on(sailor,P2), T) :- o(move_sailor(P),T), h(on(sailor,P2), T), time(T), positions(P), positions(P2), not h(on(sailor,P), T).

% Action: move_something
  % Move the object in question
h(on(E,P), T+1) :- o(move_something(E,P), T), time(T), positions(P), entities(E),
    E != sailor, not h(on(E,P), T).
ab(on(E,P2), T) :- o(move_something(E,P), T), h(on(E,P2), T), time(T),
    positions(P), positions(P2), entities(E), E != sailor, not h(on(E,P), T).
  % Move the sailor too
h(on(sailor,P), T+1) :- o(move_something(E,P), T), time(T), positions(P),
    entities(E), not h(on(E,P), T).
ab(on(sailor,P2), T) :- o(move_something(E,P), T), h(on(sailor,P2), T),
    time(T), positions(P), positions(P2), not h(on(E,P), T).

% Executability conditions
  % Can't move something if the sailor isn't on the same side as it
exec(move_sailor(P),T) :- time(T), positions(P), not h(on(sailor, P), T).
  % Can't move something to where it already is
exec(move_something(E,P), T) :- time(T), positions(P), positions(P2), entities(E),
    h(on(E,P2),T), h(on(sailor,P2),T), not h(on(E,P), T).
:- actions(A), time(T), not exec(A,T), o(A,T).

% Generate all possible actions
1 {o(A,T) : actions(A)} 1 :- ptime(T).

% Define the goal
goal(T) :- time(T), h(on(goat,far),T), h(on(wolf,far),T), h(on(cabbage,far),T).

% Define fail states
badState(T) :- time(T), positions(G), positions(W), positions(S), positions(C),
    h(on(goat,G),T), h(on(wolf,W),T), h(on(sailor,S),T), h(on(cabbage,C),T),
    G = W, S != W.
badState(T) :- time(T), positions(G), positions(W), positions(S), positions(C),
    h(on(goat,G),T), h(on(wolf,W),T), h(on(sailor,S),T), h(on(cabbage,C),T),
    G = C, S != G.

% Exclude any set that hasn't reached the goal by time 8
:- not goal(8).
% Exclude any set that was ever in a fail state
:- badState(T), time(T).

% Display the actions needed to reach the goal
#show o/2.
