# -*- coding: latin-1 -*-
from numpy import *
from math import *

def amp(n):
  l=[1]
  for i in range(1,n):
    l.append(0)
  for k in range(1,n):
    m=l[:]
    for j in range(0,n-1):
      if m[j]==1:
        if l[j+1]==1:
          l[j+1]=0
        else:
          l[j+1]=1
  return sum(l)
  
if __name__ == "__main__":

  # Initilaisation :
  n = 1001
  t = zeros(n)
  t[0] = 1
  while (t[n-1] == 0):
    for i in range (n-2,-1,-1):
      if (t[i] == 1):
        if (t[i+1] == 0):
          t[i+1] = 1
        else:
          t[i+1] = 0
  s = sum(t)
  print(s)
  
  print(amp(1001))
