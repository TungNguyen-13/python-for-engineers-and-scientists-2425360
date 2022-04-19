import math

import numpy as np
import matplotlib.pyplot as pp

# Initialise Phi
n = 64
phi = np.zeros((n, n), dtype='float')

phi[-1, :] = 1

# Show the transpose of Phi
pp.imshow(phi.T, origin='lower', extent=(0, 1, 0, 1))

# Set initial conditions
# Set 0 conditions to the bottom and left edges
# Set sinousdoial condition to the top and right edge

dx = 1 / n
xs = np.linspace(0.5 * dx, 1 - 0.5 * dx, n)
print(xs.size)

phi[:, -1] = np.sin(2 * math.pi * xs)
phi[-1, :] = np.sin(2 * math.pi * xs)

pp.imshow(phi.T, origin='lower', extent=(0, 1, 0, 1))

pp.show()
