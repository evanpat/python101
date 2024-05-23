from numpy import random as np
import matplotlib.pyplot as plt
import seaborn as sns

normal_dist = np.normal(size=10000)

sns.distplot(normal_dist, hist=False)

plt.show()