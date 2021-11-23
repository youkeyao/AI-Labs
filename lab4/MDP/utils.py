import bisect
import collections
import collections.abc
import functools
import heapq
import operator
import os.path
import random
from itertools import chain, combinations
from statistics import mean

import numpy as np

def vector_add(a, b):
    """Component-wise addition of two vectors."""
    return tuple(map(operator.add, a, b))


orientations = EAST, NORTH, WEST, SOUTH = [(1, 0), (0, 1), (-1, 0), (0, -1)]
turns = LEFT, RIGHT = (+1, -1)


def turn_heading(heading, inc, headings=orientations):
    return headings[(headings.index(heading) + inc) % len(headings)]


def turn_right(heading):
    return turn_heading(heading, RIGHT)


def turn_left(heading):
    return turn_heading(heading, LEFT)


def expected_utility(a, s, U, mdp):
    """
    Compute the expected utility of doing a in state s, according to the MDP and U.
    
    paras: the q-state (state s, action a), current utilities U, the MDP mdp

    return: the expected utility of doing a in state s, according to the MDP and U.

    """

    q = 0
    R, T, gamma = mdp.R, mdp.T, mdp.gamma
    for p in T(s, a):
        q += p[0] * (R(p[1]) + gamma * U[p[1]])
    return q
