from functools import reduce

def fibonacciList(n):
    return [[0] * x for x in reduce(lambda x,y: x+[x[-2]+x[-1]], range(1,n-1), [0,1])]