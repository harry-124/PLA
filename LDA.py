#!/usr/bin/env python
import numpy as np
from numpy import linalg as LA
import math as m
import matplotlib.pyplot as plt

x1=np.array([[1.08,0.75,0.85,0.94,0.40,1.25,1.19,0.99,0.69,1.32],[0.08,-0.19,-0.11,0.00,-0.09,-0.21,0.07,0.04,-0.02,0.02]])
x2=np.array([[0.01,-0.01,0.09,-0.05,-0.45,0.07,-0.33,-0.06,-0.33,-0.24],[0.85,1.05,0.93,1.41,1.45,1.20,0.88,1.08,1.10,1.01]])
C1=np.zeros((2,1))
C2=np.zeros((2,1))
C=np.zeros((2,1))
for i in range(0,10):
    x1_comp=np.array([[x1[0][i]],[x1[1][i]]])
    x2_comp=np.array([[x2[0][i]],[x2[1][i]]])
    C1=C1+x1_comp
    C2=C2+x2_comp
C1=C1/10.0
C2=C2/10.0
C=(C1+C2)/2.0
#Between class scatter matrix
SB=np.zeros((2,2))
SB=((C1-C).dot((C1-C).transpose()) + (C2-C).dot((C2-C).transpose()))/2.0

#Within class scatter matrix
S1=np.zeros((2,2))
S2=np.zeros((2,2))
SW=np.zeros((2,2))
for i in range(0,10):
    x1_comp=np.array([[x1[0][i]],[x1[1][i]]])
    x2_comp=np.array([[x2[0][i]],[x2[1][i]]])
    S1=S1 + (x1_comp-C1).dot((x1_comp-C1).transpose())
    S2=S2 + (x2_comp-C2).dot((x2_comp-C2).transpose())
SW=(S1 + S2)/2.0



#Finding eigenvector
w,E = LA.eig((LA.inv(SW)).dot(SB))
y1=np.zeros((2,10))
y2=np.zeros((2,10))
E[0][0],E[0][1]=E[0][1],E[0][0]
E[1][0],E[1][1]=E[1][1],E[1][0]
y1=(E.transpose()).dot(x1)
y2=(E.transpose()).dot(x2)




#Reconstruction

r1=np.zeros((2,10))
r2=np.zeros((2,10))
r1=E.dot(y1)
r2=E.dot(y2)
print(r1)
print(r2)

'''
#x2=np.zeros((2,12))
#x2[0]=y[0]*v[0][0]
#x2[1]=y[0]*v[0][1]
'''

n=np.zeros(10)
m=E[0][1]/E[0][0]
print(m)
plt.scatter(y1[0],n,color='g')
plt.scatter(y2[0],n,color='r')
plt.grid()
plt.show()

