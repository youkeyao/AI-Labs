from os import stat

from numpy import index_exp
from problem import Direction
import math
import time

class SearchAlgorithm:
    def __init__(self, algo_name):
        assert algo_name in ["tiny", "bfs", "dfs", "Exercise2_1_1", "Exercise2_1_2", "Exercise2_2_1", "Exercise2_2_2", "Exercise2_3_1"], "Invalid algorithm."

        if algo_name == "tiny":
            self._solver = tiny_maze_search
        elif algo_name == "bfs":
            self._solver = breadth_first_search
        elif algo_name == "dfs":
            self._solver = depth_first_search

        # for Lab 2
        elif algo_name == "Exercise2_1_1":
            self._solver = Exercise2_1_1
        elif algo_name == "Exercise2_1_2":
            self._solver = Exercise2_1_2
        elif algo_name == "Exercise2_2_1":
            self._solver = Exercise2_2_1
        elif algo_name == "Exercise2_2_2":
            self._solver = Exercise2_2_2
        elif algo_name == "Exercise2_3_1":
            self._solver = Exercise2_3_1

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

# ****************************** For Lab 2 ******************************

def Exercise2_1_1(problem):
    """
    Returns the number of lakes using depth-first graph search (DFGS).

    Please note that some APIs in the environment of Lab 2 are slightly different from them in the environment of Lab 1.
    """
    from util import Stack

    lakes = 0
    explored = []
    blank = Stack()
    lakes = Stack()
    blank.push(problem.get_start())

    while True:
        if blank.is_empty():
            return lakes

        now_blank = blank.pop()
        explored.append(now_blank)
        blank_successors = problem.get_successors(now_blank)
        lake_successors = problem.get_successors(now_blank, 1)

        for succ in blank_successors:
            if not succ[0] in explored:
                blank.push(succ[0])
        for succ in lake_successors:
            if not succ[0] in explored:
                lakes += 1
                lakes.push(succ[0])
                while not lakes.is_empty():
                    now_lake = lakes.pop()
                    explored.append(now_lake)
                    successors = problem.get_successors(now_lake, 1)
                    for s in successors:
                        if not s[0] in explored:
                            lakes.push(s[0])

def increase_depth1(depth):
    return depth + 1

def increase_depth2(depth):
    return depth * 2

def Exercise2_1_2(problem):
    """
    Returns the path from S to G using DFGS with the iterative deepening trick.
    """
    from util import Stack

    depth = 1
    flag = True
    while flag:
        flag = False
        explored = []
        s = Stack()
        s.push((problem.get_start(), [], 0))

        while True:
            if s.is_empty():
                break

            now = s.pop()
            explored.append(now[0])
            if problem.is_goal(now[0]):
                return now[1]
            
            if now[2] + 1 < depth:
                successors = problem.get_successors(now[0])
                for succ in successors:
                    if not succ[0] in explored:
                        s.push((succ[0], now[1] + [succ[1]], now[2] + 1))
            else:
                flag = True
        
        depth = increase_depth2(depth)

def Exercise2_2_1(problem):
    """
    Returns the least-cost path from S to G and its cost using uniform-cost graph search (UCGS)
    """
    from queue import PriorityQueue
    
    count = 0
    explored = []
    s = PriorityQueue()
    s.put((0, count, problem.get_start(), []))

    while True:
        if s.empty():
            return []

        now = s.get()
        explored.append(now[2])
        if problem.is_goal(now[2]):
            return (now[0], now[3])
        successors = problem.get_successors(now[2])
        for succ in successors:
            if not succ[0] in explored:
                count += 1
                s.put((now[0] + succ[2], count, succ[0], now[3] + [succ[1]]))

def Heuristic1(state1, state2): # the first heuristic function using Euclidean distance
    return math.sqrt(math.pow(state1[0] - state2[0], 2) + math.pow(state1[1] - state2[1], 2))

def Exercise2_2_2(problem):
    """
    Returns the path from S to G using greedy graph search (GGS).
    """
    from queue import PriorityQueue
    
    count = 0
    explored = []
    s = PriorityQueue()
    s.put((Heuristic1(problem.get_start(), problem.get_goal()), count, problem.get_start(), []))

    while True:
        if s.empty():
            return []

        now = s.get()
        explored.append(now[2])
        if problem.is_goal(now[2]):
            return now[3]
        successors = problem.get_successors(now[2])
        for succ in successors:
            if not succ[0] in explored:
                count += 1
                s.put((Heuristic1(succ[0], problem.get_goal()), count, succ[0], now[3] + [succ[1]]))

def Heuristic2(state1, state2): # the second heuristic function
    indicator = 0
    if abs(state1[0] - state2[0]) != abs(state1[1] - state2[1]):
        indicator = 1
    return abs(state1[0] - state2[0]) + abs(state1[1] - state2[1]) - indicator

def Exercise2_3_1(problem):
    """
    Returns the least-cost path from S to G and its cost using a-star graph search (ASGS)
    """
    from queue import PriorityQueue
    
    count = 0
    explored = []
    s = PriorityQueue()
    s.put((Heuristic2(problem.get_start(), problem.get_goal()), count, problem.get_start(), [], 0))

    while True:
        if s.empty():
            return []

        now = s.get()
        explored.append(now[2])
        if problem.is_goal(now[2]):
            return (now[4], now[3])
        successors = problem.get_successors(now[2])
        for succ in successors:
            if not succ[0] in explored:
                count += 1
                g = now[4] + succ[2]
                h = Heuristic2(succ[0], problem.get_goal())
                s.put((g + h, count, succ[0], now[3] + [succ[1]], g))