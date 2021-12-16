import numpy as np

if __name__ == "__main__":
    X = np.load('Data1_X.npy')
    Y = np.load('Data1_Y.npy')
    """Your code here"""
    X = np.matrix(X)
    Y = np.matrix(Y)
    Y_hat = X * (X.T * X).I * X.T * Y
    print(Y_hat)