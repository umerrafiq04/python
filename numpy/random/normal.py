# Generate a random normal distribution of size 2x3 with mean at 1 and standard deviation of 2:

from numpy import random
import numpy as np

x = random.normal(loc=1, scale=2, size=(2, 3))
print(np.mean(x))
print(x)