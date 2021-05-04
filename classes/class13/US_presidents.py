import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read data from relative directory
data = pd.read_csv('data/president_heights.csv', index_col='order')

# Pandas dataframe
print(data.head())

# plot heights as histogram
heights = np.array(data['height(cm)'])
# plt.hist(heights)
# plt.show()

import seaborn; seaborn.set() # set plot style

plt.hist(heights)
plt.title('Height Distribution of US Presidents')
plt.xlabel('height (cm)')
plt.ylabel('number')
plt.show()