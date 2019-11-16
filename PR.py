#!/usr/bin/env python
import numpy as np
from numpy import linalg as LA
import math as m
x=np.array([[0.67,0.71,0.48,0.72,0.29,0.89,-1.07,-2.94,0.33,1.38],[-1.2,1.63,1.03,-0.3,-0.78,-1.15,-0.81,1.44,-0.75,-1.71]])
C=np.array([[0.9,0.1],[0.1,0.9]])
w, v = LA.eig(C)
print(w,v)
v=np.array(v)
v=v.transpose()
#v[0]=v[0]*m.sqrt(w[0])
#v[1]=v[1]*m.sqrt(w[1])
y=v.dot(x)
mean=np.zeros((2,1))
cov_comp=np.zeros((2,2))
for i in range(0,10):
    y_comp=np.array([[y[0][i]],[y[1][i]]])
    mean=mean+y_comp
    cov_comp=cov_comp+y_comp.dot(y_comp.transpose())
mean=mean/10.0
cov_comp=cov_comp/10.0
cov=cov_comp-mean.dot(mean.transpose())
print(cov)

