import numpy
n, m = map(int, input().split())
array = numpy.array([input().strip().split() for _ in range(n)], int)
print(numpy.max(numpy.min(array, axis=1), axis=0))
