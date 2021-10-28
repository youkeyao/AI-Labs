import random

from util import argmin_random_tie

def min_conflicts_value(csp, var, current):
    """Return the value that will give var the least number of conflicts.
    If there is a tie, choose at random."""
    return argmin_random_tie(csp.domains[var], key=lambda val: csp.nconflicts(var, val, current))

def min_conflicts(csp, max_steps=100000):
    """Solve a CSP by Hill Climbing on the number of conflicts."""
    """ YOUR CODE HERE """
    assignment = {}
    for v in csp.variables:
        csp.assign(v, min_conflicts_value(csp, v, assignment), assignment)

    for i in range(max_steps):
        vars = csp.conflicted_vars(assignment)
        print(len(vars))
        if not vars:
            return assignment
        var = random.choice(vars)
        val = min_conflicts_value(csp, var, assignment)
        csp.assign(var, val, assignment)

    return None