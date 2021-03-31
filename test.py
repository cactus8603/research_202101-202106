import pandas as pd, numpy as np

A = np.array([[ 0,  1,  12],
              [ 1,  1,  8],
              [ 2,  3, 10],
              [ 3,  3, 14]])
# ans = 8 + 4 + 0 + -4 = 8
# 1 , 2,
B = A[(A[:, 2]>=10)]
C = A[A[:, 2]<10]

print(B)
print(C)