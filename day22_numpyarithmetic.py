import numpy as np
n,m=map(int,input().split())
a,b=[],[]
for i in range(n):
    t=list(map(int,input().split()))
    a.append(t)
for j in range(n):
    t=list(map(int,input().split()))
    b.append(t)
a,b=np.array(a),np.array(b)
print(np.add(a,b))
print(np.subtract(a,b))
print(np.multiply(a,b))
print(a//b)
print(np.mod(a,b))
print(np.power(a,b))