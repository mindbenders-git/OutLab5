import functools as ft
import sys

def Fib(n):
	primes = ft.reduce(lambda y,x:y - set(range(x*2, n, x)) if x in y else y, range(2,int(n*(1/2)) + 1),set(range(2,n)))
	print(list(primes))


Fib(int((sys.argv)[1]))


