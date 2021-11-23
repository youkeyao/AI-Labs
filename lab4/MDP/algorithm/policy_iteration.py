import random

from algorithm.value_iteration import best_policy
from utils  import expected_utility
import matplotlib.pyplot as plt

def policy_iteration(mdp):
    """
    Solve an MDP by policy iteration [You may refer to Lecture 6, Slide 72 and Figure 17.7 in the reference book]
    
    paras: an MDP

    return: utilities, policy
    """
    x = [0]
    y0 = [0]
    y1 = [0]
    y2 = [0]
    y3 = [0]
    y4 = [0]
    y5 = [0]
    y6 = [0]
    count = 0
    U = {s: 0 for s in mdp.states}
    pi = {s: random.choice(mdp.actions(s)) for s in mdp.states}

    while True:
        U = policy_evaluation(pi, mdp)
        convergent, pi = policy_improvement(pi, U, mdp)
        count += 1
        x.append(count)
        y0.append(U[(0,0)])
        y1.append(U[(1,0)])
        y2.append(U[(0,1)])
        y3.append(U[(1,1)])
        y4.append(U[(3,0)])
        y5.append(U[(1,3)])
        y6.append(U[(3,2)])
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
    return [U, pi]

def policy_evaluation(pi, mdp, iteration_num=50):
    """
    Return an updated utility mapping U from each state in the MDP to its
    utility [You may refer to idea 1 in Lecture 6, Slide 75 and Figure 17.7 in the reference book]
    
    paras: current policy pi, mdp

    return: utilities
    """
    U = {s: 0 for s in mdp.states}
    R, T, gamma = mdp.R, mdp.T, mdp.gamma
    for i in range(iteration_num):
        for s in mdp.states:
            q = 0
            for p in T(s, pi[s]):
                q += p[0] * (R(p[1]) + gamma * U[p[1]])
            U[s] = q
    return U

def policy_improvement(pi, U, mdp):
    """
    Conduct policy improvement [You may refer to Lecture 6, Slide 72 and Figure 17.7 in the reference book]
    
    paras: current policy pi, current utilities U, the MDP mdp

    return: a bool variable which indicates whether the policy improvement is convergent, an improved policy of policy pi
    """

    pi_new = best_policy(mdp, U)
    convergent = pi_new == pi
    return [convergent, pi_new]