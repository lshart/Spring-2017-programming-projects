% Luke S. Hart
% CSE 471: Intro to AI
% Project 4: Puzzle 1

% Define the possible values for the appropriate fields
salaries(8; 10; 12; 14).
men(alan; brian; charles; derek).
jobs(mp; doctor; vet; lawyer).

% Generate all possible combinations
1 {hasJob(M,J): jobs(J)} 1 :- men(M).
1 {hasSalary(M,S): salaries(S) } 1 :- men(M).

% Remove combinations with duplicate jobs or starting salaries
:- jobs(J), men(M), men(M2), hasJob(M,J), hasJob(M2, J), M != M2.
:- salaries(J), men(M), men(M2), hasSalary(M,J), hasSalary(M2, J), M != M2.

% The MP earned the most
:- men(M), men(M2), salaries(S), salaries(S2),
hasJob(M,mp), hasSalary(M,S), hasSalary(M2, S2), S < S2.

% Alan earned more than Brian
:- hasSalary(alan, S), hasSalary(brian, S2), S < S2.

% The doctor earned more than Derek
:- men(M), hasJob(M, doctor), hasSalary(M, S), salaries(S),
hasSalary(derek, S2), S < S2.

% Derek is a vet and Brian is a lawyer
:- hasJob(M,vet), men(M), M != derek.
:- hasJob(M,lawyer), men(M), M != brian.

% Brian and Derek both didn't start at 10 thousand
:- hasSalary(M,10), men(M), M == brian.
:- hasSalary(M,10), men(M), M == derek.

% Display answer
nameJobSalary (N,J,S):- hasJob(N,J), hasSalary(N,S).
#show nameJobSalary/3.
