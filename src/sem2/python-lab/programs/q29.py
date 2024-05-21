# Create a .csv file (with contents like age, weight and BMI). Read the content of the file and using Pandas and
# MatPlotLib, plot the histogram.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

bmi = data["BMI"]
grp_size = 2
average_group_bmi = np.array([
    sum(bmi[i:i + grp_size]) / grp_size for i in range(0, len(bmi), grp_size)
])

bins = data["Age"][0:len(data["Age"]):grp_size]
plt.hist(bins[:-1], bins, weights=average_group_bmi[:-1], fill=False)

plt.show()
