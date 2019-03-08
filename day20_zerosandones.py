'''Sample Input 0

3 3 3
Sample Output 0

[[[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]]
[[[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]]'''


import numpy as np
n, m, p = map(int, input().strip().split())
for i in range(0,n):
    print(np.zeros((m,p),dtype=np.int))
for i in range(0,n):
    print(np.ones((m,p),dtype=np.int))