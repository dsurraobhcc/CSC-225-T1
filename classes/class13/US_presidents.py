import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read data from relative directory
data = pd.read_csv('data/president_heights.csv', index_col='order')

# Pandas dataframe
print(data.head())

# convert pandas Series to numpy array
heights = np.array(data['height(cm)'])
plt.hist(heights)

plt.ioff()
plt.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Matplotlib plot.
plt.show()