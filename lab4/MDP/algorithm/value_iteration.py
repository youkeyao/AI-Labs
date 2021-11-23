from icecream import ic
from utils import expected_utility
import matplotlib.pyplot as plt

def value_iteration(mdp, epsilon=0.001):
    """
    Solving an MDP by value iteration. [You may refer to Lecture 6, Slide 55 and Figure 17.4 in the reference book]
    
    paras: an MDP, an accuracy parameter epsilon which indicates the maximum change in the utility of any state in an iteration

    return: utilities, the optimal policy (to extract the optimal policy, you may use the best_policy() function)
    """
    x = [0]
    y0 = [0]
    y1 = [0]
    y2 = [0]
    y3 = [0]
    y4 = [0]
    y5 = [0]
    y6 = [0]

    U1 = {s: 0 for s in mdp.states}
    count = 0
    while True:
        convergent = True
        for s in mdp.states:
            qs = [expected_utility(a, s, U1, mdp) for a in mdp.actions(s)]
            v = max(qs)
            if -epsilon > v - U1[s] or v - U1[s] > epsilon:
                convergent = False
            U1[s] = v
        count += 1
        x.append(count)
        y0.append(U1[(0,0)])
        y1.append(U1[(1,0)])
        y2.append(U1[(0,1)])
        y3.append(U1[(1,1)])
        y4.append(U1[(3,0)])
        y5.append(U1[(1,3)])
        y6.append(U1[(3,2)])
        if convergent:
            break
    print(x)
    print(y0)
    print(y1)
    print(y2)
    print(y3)
    print(y4)
    print(y5)
    print(y6)
    plt.xlabel('iteration times')
    plt.ylabel('utility')
    plt.plot(x, y0)
    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.plot(x, y3)
    plt.plot(x, y4)
    plt.plot(x, y5)
    plt.plot(x, y6)
    plt.legend(['S0', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6'])
    plt.show()
    return [U1, best_policy(mdp, U1)]

def best_policy(mdp, U):
    """
    Conduct policy extraction by using the function expected_utility(). Given an MDP and a utility function U, determine the best policy,
    as a mapping from state to action. [You may refer to Lecture 6, Slide 66]
    
    paras: an MDP, utilities U

    return: the extracted best policy
    """

    policy = {}
    for s in mdp.states:
        actions = mdp.actions(s)
        qs = [expected_utility(a, s, U, mdp) for a in actions]
        bestq = max(qs)
        bestIndex = qs.index(bestq)
        policy[s] = actions[bestIndex]
    return policy