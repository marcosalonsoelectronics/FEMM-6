# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 11:17:11 2022

@author: Alonso
"""
from math import pi

u0= 4*pi*1e-7
Ac= 56.3e-6; N=80
I=1
g=0.25e-3

F= u0*Ac*N**2*I**2/(4*g**2)


print("Force (N)= ", F)


