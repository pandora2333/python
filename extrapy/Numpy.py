#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# ⒈ 利用Lagrange插值多项式 求被插值函数f(x)在点x=65处的近似值。建议：画出Lagrange插值多项式 的曲线。

import numpy as np
import matplotlib.pyplot as plt
import math

# x	0.10	0.20	0.30	0.40	0.50              0.60	0.70	0.80	0.90	1.00
# y	0.904837	0.818731	0.740818	0.670320	0.606531           0.548812	  0.496585   	0.449329	0.406570	0.367879
# m	-0.904837	-0.818731	-0.740818	-0.670320	-0.606531         -0.548812	-0.496585	-0.449329	-0.406570	-0.367879
x = [0.10,0.20,0.30,0.40,0.50,0.60,0.70,0.80,0.90,1.00]
y = [0.904837,0.818731,0.740818,0.670320,0.606531,0.548812,0.496585,0.449329,0.406570,0.367879]
m = [-0.904837,-0.818731,-0.740818,-0.670320,-0.606531,-0.548812,-0.496585,-0.449329,-0.406570,-0.367879]
## m = -y

long = len(x)

def l2(key,k):
    l =1
    for n in range(long):
        if k!=n:
           l = l*((key-x[n])/(x[k]-x[n]))

    return l*l

def i(j):
    i=0
    for k in range(long):
        if k!=j:
            i = i+1/x[j]-x[k]

    return i

def alpha(key,j):
    return (1-(2*(key-x[j])*i(j))) *l2(key,j)

def beta(key,j):
    return (key-x[j])*l2(key,j)

def Hermite(key):
    finall = 0
    for j in range(long):
        finall = finall + (y[j]*alpha(key,j)+m[j]*beta(key,j))
    return finall

key =  0.55
h = Hermite(key)
print(h)



plt.plot(x,y,color = 'red')
plt.show()

input()
