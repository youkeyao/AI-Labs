from .value_order import lcv
from .variable_order import mrv


def backtracking(
    csp,
    select_unassigned_variable=mrv,
    order_domain_values=lcv
):
    def backtrack(assignment):
        if len(assignment) == len(csp.variables):
            return assignment
        var = select_unassigned_variable(assignment, csp)
        for value in order_domain_values(var, assignment, csp):
            if csp.nconflicts(var, value, assignment) == 0:
                csp.assign(var, value, assignment)
                result = backtrack(assignment)
                if result != None:
                    return result
                csp.unassign(var, assignment)
        return None

    result = backtrack({})
    assert result is None or csp.goal_test(result)
    return result

def backtracking_with_inference(
    csp,
    inference,
    select_unassigned_variable=mrv,
    order_domain_values=lcv
):
    def backtrack(assignment):
        """ YOUR CODE HERE """
        if len(assignment) == len(csp.variables):
            return assignment
        var = select_unassigned_variable(assignment, csp)
        for value in order_domain_values(var, assignment, csp):
            if csp.nconflicts(var, value, assignment) == 0:
                removals = csp.suppose(var, value)
                csp.assign(var, value, assignment)
                inference(csp, var, value, assignment, removals)
                result = backtrack(assignment)
                if result != None:
                    return result
                csp.unassign(var, assignment)
                csp.restore(removals)
        return None

    result = backtrack({})
    assert result is None or csp.goal_test(result)
    return result