# -*- coding: latin-1 -*-
from numpy import *

if __name__ == "__main__":

  # Initilaisation :
  n = 7
  t = zeros(n)
  t[0] = 1
  t_aux = t.copy()
  while (t[n-1] == 0):
    for i in range (0,n):
      if (t[i] == 1):
        if (t_aux[i+1] == 0):
          t_aux[i+1] = 1
        else:
          t_aux[i+1] = 0
    t = t_aux.copy()
  s = sum(t)
  print(s)
