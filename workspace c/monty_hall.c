#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define NUM_TRIALS 100000

int main()
{
  int i;
  int numWins;
  int door;
  int doorChoice;
  int switchChoice;
  int option1, option2;
  time_t t;

  srand((unsigned) time(&t));
  numWins = 0;

  for(i = 0; i < NUM_TRIALS; i++)
  {
    door = rand() % 3;
    doorChoice = rand() % 3;

    if (door == doorChoice)
    {
      if (doorChoice == 2)
      {
        option1 = 0;
        option2 = 1;
      }
      else if (doorChoice == 1)
      {
        option1 = 0;
        option2 = 2;
      }
      else
      {
        option1 = 1;
        option2 = 2;
      }

      if (rand()%2 == 0)
        switchChoice = option1;
      else
        switchChoice = option2;
    }
    else
    {
      switchChoice = door;
    }

    doorChoice = switchChoice;
    if (doorChoice == door)
      numWins++;
  }

  printf("%d\n", numWins);
}
