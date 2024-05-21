# Create a .csv file (with contents like age, weight and BMI). Read the content of the file and using Pandas and
# MatPlotLib, plot the graph.

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot(data["Weight"], data["Height"], data["BMI"], "ko", linewidth=1)

plt.show()
