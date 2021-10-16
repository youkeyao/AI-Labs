from problem import Direction


class SearchAlgorithm:
    def __init__(self, algo_name):
        assert algo_name in ["tiny", "bfs", "dfs"], "Invalid algorithm."

        if algo_name == "tiny":
            self._solver = tiny_maze_search
        elif algo_name == "bfs":
            self._solver = breadth_first_search
        elif algo_name == "dfs":
            self._solver = depth_first_search

    def __call__(self, problem):
        return self._solver(problem)


def tiny_maze_search(problem):
    """Returns a sequence of moves that solves tinyMaze."""
    s = Direction.SOUTH
    w = Direction.WEST
    return  [s, s, w, s, w, w, s, w]

def depth_first_search(problem):
    """Returns a sequence of moves that solves general maze problems with DFS.

    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. To get started, you might leverage your Stack structure and the APIs
    provided in the Problem class:

    print("Start:", problem.get_start())
    print("Is the start a goal?", problem.is_goal(problem.get_start()))
    print("Start's successors:", problem.get_successors(problem.get_start()))
    """
    from util import Stack

    explored = []
    s = Stack()
    s.push((problem.get_start(), []))

    while True:
        if s.is_empty():
            return []

        now = s.pop()
        explored.append(now[0])
        if problem.is_goal(now[0]):
            return now[1]
        successors = problem.get_successors(now[0])
        for succ in successors:
            if not succ[0] in explored:
                s.push((succ[0], now[1] + [succ[1]]))

def breadth_first_search(problem):
    """Returns a sequence of moves that solves general maze problems with BFS.

    Search the shallowest nodes in the search tree first.
    """
    from util import Queue

    explored = []
    s = Queue()
    s.push((problem.get_start(), []))

    while True:
        if s.is_empty():
            return []

        now = s.pop()
        explored.append(now[0])
        if problem.is_goal(now[0]):
            return now[1]
        successors = problem.get_successors(now[0])
        for succ in successors:
            if not succ[0] in explored:
                s.push((succ[0], now[1] + [succ[1]]))