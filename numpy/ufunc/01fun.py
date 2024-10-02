x=[1,2,3,4,5]
y=[1,2,3,4,5]
z=[]
# with python
# for i,j in zip(x,y):
#     z.append(i+j)

# with numpy
import numpy as np
z=np.add(x,y)
print(z)
