# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """
    def __init__(self):
        self.explorAtrix = None

    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """

        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"
        pacPos = gameState.getPacmanPosition()
        self.explorAtrix[pacPos[0]][pacPos[1]] += 1

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        oldFood = currentGameState.getFood()
        newGhostStates = successorGameState.getGhostPositions()
#        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        if self.explorAtrix == None:
            self.explorAtrix = [[0 for x in range(oldFood.height)] for y in range(oldFood.width)]

        stateScore = -self.explorAtrix[newPos[0]][newPos[1]]
        if action == 'South' or action == 'West':
            if self.explorAtrix[newPos[0]][newPos[1]] == 0:
                stateScore += 1
        if newPos in oldFood.asList():
            stateScore += 1
        if action == 'Stop':
            stateScore -= 50
        if newPos in newGhostStates:
            stateScore -= 100

        return stateScore

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """

        max_choice = -99999
        chosenAct = None
        for act in gameState.getLegalActions():
            nextState = gameState.generateSuccessor(0, act)
            nextVal = self.miniMax(nextState, self.depth, 1)
            if nextVal > max_choice:
                max_choice = nextVal
                chosenAct = act

        return chosenAct

    def miniMax(self, gameState, currDepth, agentIndex):
        if currDepth == 0 or gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)
        if agentIndex == 0:
            best_Val = -99999
            for act in gameState.getLegalActions(agentIndex):
                nextState = gameState.generateSuccessor(agentIndex, act)
                newVal = self.miniMax(nextState, currDepth, agentIndex + 1)
                best_Val = max(best_Val, newVal)
            return best_Val
        if agentIndex > 0 and agentIndex < gameState.getNumAgents() - 1:
            best_Val = 99999
            for act in gameState.getLegalActions(agentIndex):
                nextState = gameState.generateSuccessor(agentIndex, act)
                newVal = self.miniMax(nextState, currDepth, agentIndex + 1)
                best_Val = min(best_Val, newVal)
            return best_Val
        if agentIndex == gameState.getNumAgents() - 1:
            best_Val = 99999
            for act in gameState.getLegalActions(agentIndex):
                nextState = gameState.generateSuccessor(agentIndex, act)
                newVal = self.miniMax(nextState, currDepth - 1, 0)
                best_Val = min(best_Val, newVal)
            return best_Val


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        alpha = -99999
        beta = 99999
        v = -99999
        chosenAct = None
        for act in gameState.getLegalActions():
            nextState = gameState.generateSuccessor(0, act)
            nextVal = max(v, self.alphaBetica(nextState, self.depth, 1, alpha, beta))
            if nextVal > v:
                v = nextVal
                chosenAct = act
            alpha = max(alpha, v)

        return chosenAct

    def alphaBetica(self, gameState, currDepth, agentIndex, alpha, beta):
        if currDepth == 0 or gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)
        if agentIndex == 0:
            best_Val = -99999
            for act in gameState.getLegalActions(agentIndex):
                nextState = gameState.generateSuccessor(agentIndex, act)
                newVal = self.alphaBetica(nextState, currDepth, agentIndex + 1, alpha, beta)
                best_Val = max(best_Val, newVal)
                if best_Val > beta:
                    return best_Val
                alpha = max(alpha, best_Val)
            return best_Val
        if agentIndex > 0 and agentIndex < gameState.getNumAgents() - 1:
            best_Val = 99999
            for act in gameState.getLegalActions(agentIndex):
                nextState = gameState.generateSuccessor(agentIndex, act)
                newVal = self.alphaBetica(nextState, currDepth, agentIndex + 1, alpha, beta)
                best_Val = min(best_Val, newVal)
                if best_Val < alpha:
                    return best_Val
                beta = min(beta, best_Val)
            return best_Val
        if agentIndex == gameState.getNumAgents() - 1:
            best_Val = 99999
            for act in gameState.getLegalActions(agentIndex):
                nextState = gameState.generateSuccessor(agentIndex, act)
                newVal = self.alphaBetica(nextState, currDepth - 1, 0, alpha, beta)
                best_Val = min(best_Val, newVal)
                if best_Val < alpha:
                    return best_Val
                beta = min(beta, best_Val)
            return best_Val

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
