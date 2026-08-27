

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
a = int(input("Enter 1st element in the matrix: "))
b = int(input("Enter 2nd element in the matrix: "))
c = int(input("Enter 3rd element in the matrix: "))
order = int(input("Enter the order of the matrix: "))
def poly(a,b,c, order):

  x = np.array([a,b,c])
  x = x.reshape(3,1)
  original_x = x
  for i in range(2, order + 1):

    x = np.hstack((x, original_x**i))



  x = np.hstack((np.ones(shape=(len(x),1)),x))
  return x
poly(a,b,c,order)
