#!/usr/bin/env python
import numpy as np
from numpy import linalg as LA
import math as m
import matplotlib.pyplot as plt

x1=np.array([[1.08,0.75,0.85,0.94,0.40,1.25,1.19,0.99,0.69,1.32],[0.08,-0.19,-0.11,0.00,-0.09,-0.21,0.07,0.04,-0.02,0.02]])
x2=np.array([[0.01,-0.01,0.09,-0.05,-0.45,0.07,-0.33,-0.06,-0.33,-0.24],[0.85,1.05,0.93,1.41,1.45,1.20,0.88,1.08,1.10,1.01]])
z= np.linspace(-0.5,0.5,1000)
m=-1.8804819328843871

plt.plot(z,m*z,color='k')
plt.scatter(x1[0],x1[1],color='g')
plt.scatter(x2[0],x2[1],color='r')
plt.grid()
plt.show()