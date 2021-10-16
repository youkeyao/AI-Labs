import matplotlib.pyplot as plt

x = [1, 2, 4, 8]
y = [4.76837158203125e-06, 2.0503997802734375e-05, 5.269050598144531e-05, 0.0002512931823730469]
plt.plot(x, y)
plt.xlabel('depth')
plt.ylabel('memory consumption')
plt.show()