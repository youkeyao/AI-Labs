# ghostAgents.py
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


from game import Agent
from game import Actions
from game import Directions
import random
from util import manhattanDistance
import util


class GhostAgent(Agent):
    def __init__(self, index):
        self.index = index

    def getAction(self, state):
        dist = self.getDistribution(state)
        if len(dist) == 0:
            return Directions.STOP
        else:
            return util.chooseFromDistribution(dist)

    def getDistribution(self, state):
        "Returns a Counter encoding a distribution over actions from the provided state."
        util.raiseNotDefined()


class RandomGhost(GhostAgent):
    "A ghost that chooses a legal action uniformly at random."

    def getDistribution(self, state):
        dist = util.Counter()
        for a in state.getLegalActions(self.index):
            dist[a] = 1.0
        dist.normalize()
        return dist


class DirectionalGhost(GhostAgent):
    "A ghost that prefers to rush Pacman, or flee when scared."

    def __init__(self, index, prob_attack=0.8, prob_scaredFlee=0.8):
        self.index = index
        self.prob_attack = prob_attack
        self.prob_scaredFlee = prob_scaredFlee

    def getDistribution(self, state):
        # Read variables from state
        ghostState = state.getGhostState(self.index)
        legalActions = state.getLegalActions(self.index)
        pos = state.getGhostPosition(self.index)
        isScared = ghostState.scaredTimer > 0

        speed = 1
        if isScared:
            speed = 0.5

        actionVectors = [Actions.directionToVector(
            a, speed) for a in legalActions]
        newPositions = [(pos[0]+a[0], pos[1]+a[1]) for a in actionVectors]
        pacmanPosition = state.getPacmanPosition()

        # Select best actions given the state
        distancesToPacman = [manhattanDistance(
            pos, pacmanPosition) for pos in newPositions]
        if isScared:
            bestScore = max(distancesToPacman)
            bestProb = self.prob_scaredFlee
        else:
            bestScore = min(distancesToPacman)
            bestProb = self.prob_attack
        bestActions = [action for action, distance in zip(
            legalActions, distancesToPacman) if distance == bestScore]

        # Construct distribution
        dist = util.Counter()
        for a in bestActions:
            dist[a] = bestProb / len(bestActions)
        for a in legalActions:
            dist[a] += (1-bestProb) / len(legalActions)
        dist.normalize()
        return dist

def scoreEvaluationFunctionGhost(currentGameState):
    return currentGameState.getScore()

class MinimaxGhost(GhostAgent):
    def __init__(self, index, evalFn = 'scoreEvaluationFunctionGhost', depth = '2'):
        self.index = index # Ghosts are always with index > 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

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
        Returns the minimax action using self.depth, self.index and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        actions = gameState.getLegalActions(self.index)

        scores = [self.value(gameState.generateSuccessor(self.index, action), self.index+1, 0) for action in actions]
        bestScore = min(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices)

        return actions[chosenIndex]
