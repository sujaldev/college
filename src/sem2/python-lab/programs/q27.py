# Create 2 arrays, using MatPlotLib, plot the graph with the content of the two arrays, with coordinates plotted on
# x-axis and y-axis.

import numpy as np
import matplotlib.pyplot as plt

plt.plot(
    np.array([np.random.randint(0, 100) for _ in range(50)]),
    np.array([np.random.randint(0, 100) for _ in range(50)]),
    "ko"
)
plt.show()
