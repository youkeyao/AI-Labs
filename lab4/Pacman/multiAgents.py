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


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

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
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        return successorGameState.getScore()

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

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '4'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent
    """
    def value(self, gameState, index, depth):
        if index % gameState.getNumAgents() == 0:
            return self.maxValue(gameState, depth + 1)
        else:
            return self.minValue(gameState, index, depth)

    def maxValue(self, gameState, depth):
        if gameState.isLose() or gameState.isWin() or depth >= self.depth:
            return self.evaluationFunction(gameState)

        v = -10000
        for action in gameState.getLegalActions(0):
            next = gameState.generateSuccessor(0, action)
            v = max(v, self.value(next, 1, depth))
        return v

    def minValue(self, gameState, index, depth):
        if gameState.isLose() or gameState.isWin():
            return self.evaluationFunction(gameState)

        v = 10000
        for action in gameState.getLegalActions(index):
            next = gameState.generateSuccessor(index, action)
            v = min(v, self.value(next, index+1, depth))
        return v

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

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        actions = gameState.getLegalActions(0)

        scores = [self.value(gameState.generateSuccessor(0, action), 1, 0) for action in actions]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices)

        return actions[chosenIndex]

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning
    """

    def value(self, gameState, index, depth, a, b):
        if index % gameState.getNumAgents() == 0:
            return self.maxValue(gameState, depth + 1, a, b)[0]
        else:
            return self.minValue(gameState, index, depth, a, b)[0]

    def maxValue(self, gameState, depth, a, b):
        if gameState.isLose() or gameState.isWin() or depth >= self.depth:
            return [self.evaluationFunction(gameState), None]

        v = -10000
        ac = gameState.getLegalActions(0)[0]
        for action in gameState.getLegalActions(0):
            next = gameState.generateSuccessor(0, action)
            value = self.value(next, 1, depth, a, b)
            if value > v:
                v = value
                ac = action
            if v >= b:
                return [v, ac]
            a = max(a, v)
        return [v, ac]

    def minValue(self, gameState, index, depth, a, b):
        if gameState.isLose() or gameState.isWin():
            return [self.evaluationFunction(gameState), None]

        v = 10000
        ac = gameState.getLegalActions(index)[0]
        for action in gameState.getLegalActions(index):
            next = gameState.generateSuccessor(index, action)
            value = self.value(next, index+1, depth, a, b)
            if value < v:
                v = value
                ac = action
            if v <= a:
                return [v, ac]
            b = min(b, v)
        return [v, ac]

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        return self.maxValue(gameState, 0, -10000, 10000)[1]

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent
    """

    def value(self, gameState, index, depth):
        if index % gameState.getNumAgents() == 0:
            return self.maxValue(gameState, depth + 1)
        else:
            return self.expValue(gameState, index, depth)

    def maxValue(self, gameState, depth):
        if gameState.isLose() or gameState.isWin() or depth >= self.depth:
            return self.evaluationFunction(gameState)

        v = -10000
        for action in gameState.getLegalActions(0):
            next = gameState.generateSuccessor(0, action)
            v = max(v, self.value(next, 1, depth))
        return v

    def expValue(self, gameState, index, depth):
        if gameState.isLose() or gameState.isWin():
            return self.evaluationFunction(gameState)

        v = 0
        p = len(gameState.getLegalActions(index))
        for action in gameState.getLegalActions(index):
            next = gameState.generateSuccessor(index, action)
            v += self.value(next, index+1, depth) / p
        return v

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        actions = gameState.getLegalActions(0)

        scores = [self.value(gameState.generateSuccessor(0, action), 1, 0) for action in actions]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices)

        return actions[chosenIndex]
