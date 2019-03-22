import numpy
n = int(input())
arrays = [list(map(int,input().split())) for _ in range(n*2)]
print(numpy.matmul(arrays[:n],arrays[n:]))