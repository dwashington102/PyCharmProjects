import os

def fib(n):
    a,b = 0,1
    print(a,b)
    while a < n:
        print(a, end='')
        a,b = b, a+b
        print()
fib(10)


