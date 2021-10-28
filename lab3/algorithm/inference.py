def no_inference(csp, var, value, assignment, removals):
    return True

def forward_checking(csp, var, value, assignment, removals):
    """Prune neighbor values inconsistent with var=value."""
    csp.support_pruning()  # It is necessary for using csp.prune()
    """ YOUR CODE HERE """
    for v in csp.neighbors[var]:
        for val2 in csp.curr_domains[v]:
            if not csp.constraints(var, value, v, val2):
                csp.prune(v, val2, removals)

    return True

def AC3(csp, removals=None):
    def revise(Xi, Xj):
        """Return true if we remove a value."""
        """ YOUR CODE HERE """
        removed = False
        for i in csp.curr_domains[Xi]:
            consistent = False
            for j in csp.curr_domains[Xj]:
                if csp.constraints(Xi, i, Xj, j):
                    consistent = True
            if not consistent:
                csp.prune(Xi, i, removals)
                removed = True
        return removed

    queue = {(Xi, Xk) for Xi in csp.variables for Xk in csp.neighbors[Xi]}
    csp.support_pruning()  # It is necessary for using csp.prune()
    while queue:
        """ YOUR CODE HERE """
        Xi, Xj = queue.pop()
        if revise(Xi, Xj):
            for Xk in csp.neighbors[Xi]:
                queue.add((Xk, Xi))

    return True  # CSP is satisfiable

def mac(csp, var, value, assignment, removals, constraint_propagation=AC3):
    """Maintain arc consistency."""
    return constraint_propagation(csp, removals)
