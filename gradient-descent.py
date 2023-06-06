import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4, 4, 200)
y = x**2

plt.xlabel('x')
plt.ylabel('y = x^2')
plt.plot(x, y)

# learning rate
lr = 0.1
np.random.seed(20)
x_start = np.random.normal(0, 2, 1)
dy_dx_old = 2 * x_start
dy_dx_new = 0

tolerance = 1e-2
# stop once the value has converged
while abs(dy_dx_new - dy_dx_old) > tolerance:
    dy_dx_old = dy_dx_new
    x_start = x_start - lr * dy_dx_old
    dy_dx_new = 2 * x_start
    plt.scatter(x_start, x_start**2)
    plt.pause(0.5)
plt.show()