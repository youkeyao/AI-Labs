import numpy as np
import matplotlib.pyplot as plt
from utils import plot_decision_boundary

def CELoss_binary(X, y, theta):
    '''
    paras: X is a mini-batch of samples, y is the true label of the samples
        in the mini-batch, theta is the parameter we need to learn in logistic regression
    return: the binary cross entropy
    '''
    """Your code here"""
    z = X @ theta
    y_hat = 1 / (1 + np.exp(-z))
    return - (y.T @ np.log(y_hat + 0.000001) + (1-y).T @ np.log(1-y_hat + 0.000001)) / X.shape[0]

def precision(y_true, y_predict):
    '''
    paras: y_true is the true label, y_predict is the predicted label of your model
    return: the precision
    '''
    return np.sum(y_true == y_predict) / y_true.shape[0]

def predict(X, theta, threshold):
    z = X @ theta
    y_hat = 1 / (1+np.exp(-z))
    y_predict = np.zeros(y_hat.shape)
    y_predict[y_hat > threshold] = 1
    return y_predict

def gradient(X, y, theta):
    '''
    paras: X is a mini-batch of samples, y is the true label of the samples
        in the mini-batch, theta is the parameter we need to learn in logistic regression
    return: the mini-batch gradient of the binary cross entropy loss function with respect to 
        the parameter theta for a given mini-batch of samples
    '''
    """Your code here"""
    z = X @ theta
    y_hat = 1 / (1 + np.exp(-z))
    return X.T @ (y_hat-y) / X.shape[0]

if __name__ == "__main__":
    X_all, y_all = np.load('Data2_X.npy'), np.load('Data2_Y.npy')
    """Your code here"""
    b = np.ones((X_all.shape[0], 1))
    X_all = np.c_[X_all, b]

    for k in range(3):
        theta = np.ones((X_all.shape[1],))

        lr = 0.01
        iteration_num = 10000
        threshold = 0.2 + k * 0.3

        loss = []
        prec = []

        for i in range(iteration_num):
            # change algorithm
            index = np.random.choice(np.arange(X_all.shape[0]), size=100, replace=False)
            X = X_all[index]
            y = y_all[index]
            theta -= lr * gradient(X, y, theta)

            y_predict = predict(X_all, theta, threshold)

            loss.append(CELoss_binary(X_all, y_all, theta))
            prec.append(precision(y_all, y_predict))

        # plt.plot([i for i in range(iteration_num)], loss, label=str(threshold))
        # plt.plot([i for i in range(iteration_num)], prec, label=str(threshold))

        plot_decision_boundary(X_all, y_all, lambda x : predict(np.c_[x, np.ones((x.shape[0], 1))], theta, threshold))
        plt.show()

    # plt.legend()
    # plt.xlabel('iteration times')
    # plt.ylabel('precision')
    # plt.ylabel('binary cross entropy loss')

    # plt.show()