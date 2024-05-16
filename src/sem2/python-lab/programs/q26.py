# Using Pandas, create a dataframe, initialize it with the contents such as your enrollment Number and name and
# display them.

import numpy as np
import pandas as pd

class_list = pd.DataFrame(np.array([
    ["Name", "Enrollment Number"],
    ["Alice", 1],
    ["Bob", 2],
    ["Bob", 3]
]))

print(class_list)
