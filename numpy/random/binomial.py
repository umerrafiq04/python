'''Let's say you're simulating coin flips where:

You flip the coin 3 times (n=3),
Each flip has a 50% chance of landing heads (p=0.5),
You want to repeat this 3 times (size=3).
The result will be an array of 3 values, where each value represents how many "heads" (successes) occurred in 3 coin flips.

For example, the output might look like:

python
Copy code
[2, 1, 3]'''


from numpy import random

x=random.binomial(n=4,p=.5,size=(10))

print(x)