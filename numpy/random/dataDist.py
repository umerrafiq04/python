import numpy as np
from numpy import random as rd
# Question:
# Generate a 1-D array containing 100 values, where each value has to be 3, 5, 7 or 9.
# The probability for the value to be 3 is set to be 0.1
# The probability for the value to be 5 is set to be 0.3
# The probability for the value to be 7 is set to be 0.6
# The probability for the value to be 9 is set to be 0

x=rd.choice([3,5,7,9],p=[.1,.3,.6,0],size=(100))
print(x)