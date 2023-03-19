#!/usr/bin/env python
# coding: utf-8

# In[39]:



#import numpy as np

from scipy import stats
x=np.array([17,13,12,15,16,14,16,16,18,19])
y=np.array([94,73,59,80,93,85,66,79,77,91])
slope, intercept, r, p, std_err = stats.linregress(x, y)
print('r=',r)
print('b=',slope)
print('a=',intercept)


# In[ ]:





# In[34]:


print(x)


# In[35]:


print(y)


# 
# 

# In[ ]:





# In[24]:


#here we used to 1D arrays and plotted its regression line
import matplotlib.pyplot as plt
import numpy as np

from scipy import stats
x=np.array([17,13,12,15,16,14,16,16,18,19])
y=np.array([94,73,59,80,93,85,66,79,77,91])
slope, intercept, r, p, std_err = stats.linregress(x, y)
def myfunc(x):
  return slope * x + intercept
mymodel = list(map(myfunc, x))
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

