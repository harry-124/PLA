#!/usr/bin/env python
import numpy as np
from numpy import linalg as LA
import math as m
import matplotlib.pyplot as plt
X1=np.array([[1.08,0.75],[0.08,-0.19]])
X2=np.array([[0.01,0.09],[0.85,0.93]])
X=np.concatenate((X1,X2),axis=1)
z=np.zeros((2,1))
print(X)
G=np.zeros((4,4))
G1=np.zeros((4,2))
G2=np.zeros((4,2))
C1=np.zeros((4,1))
C2=np.zeros((4,1))

def kernel(x,y):
    z=x-y
    K=m.exp(-0.5*((z.transpose()).dot(z)))
    return K

for i in range(0,4):
    for j in range (0,4):
        G[i][j]=kernel(X[:,j],X[:,i])


for i in range(0,2):
    G1[:,i]=G[:,i]
    G2[:,i]=G[:,i+2]

print('Class Data 1 in HDS=',G1)
print('Class Data 2 in HDS=',G2)

for i in range(0,2):
    x1_comp=np.array([[G1[0][i]],[G1[1][i]],[G1[2][i]],[G1[3][i]]])
    x2_comp=np.array([[G2[0][i]],[G2[1][i]],[G2[2][i]],[G2[3][i]]])    
    C1=C1+x1_comp
    C2=C2+x2_comp
C1=C1/2.0
C2=C2/2.0
C=(C1+C2)/2.0
print('C1=',C1)
print('C2=',C2)
print('C=',C)

#Between class scatter matrix
SB=((C1-C).dot((C1-C).transpose()) + (C2-C).dot((C2-C).transpose()))/2.0
#Within class scatter matrix
S1=np.zeros((4,4))
S2=np.zeros((4,4))
SW=np.zeros((4,4))
for i in range(0,2):
    x1_comp=np.array([[G1[0][i]],[G1[1][i]],[G1[2][i]],[G1[3][i]]])
    x2_comp=np.array([[G2[0][i]],[G2[1][i]],[G2[2][i]],[G2[3][i]]]) 
    S1=S1 + (x1_comp-C1).dot((x1_comp-C1).transpose())
    S2=S2 + (x2_comp-C2).dot((x2_comp-C2).transpose())
SW=(S1 + S2)

#Finding eigenvector
w,E = LA.eig((LA.inv(SW)).dot(SB))
print('w=',w)
print('E=',E)

v=X.dot(E)
print(v)
A1=[[1.08,0.75,0.85,0.94,0.4,1.25,1.19,0.99,0.69,1.32],[0.08,-0.19,-0.11,0.01,-0.09,-0.21,0.07,0.04,-0.02,0.02]]
A2=[[0.01,-0.01,0.09,-0.05,-0.45,0.07,-0.33,-0.06,-0.33,-0.24],[0.85,1.05,0.93,1.41,1.45,1.20,0.88,1.08,1.10,1.01]]
a1=(v.transpose())[0].dot(A1)
a2=(v.transpose())[0].dot(A2)
print('Projected=',a1,a2)

plt.scatter(A2[0],A2[1],color='g')
plt.scatter(A1[0],A1[1],color='r')
plt.grid()
plt.show()