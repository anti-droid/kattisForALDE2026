from functools import lru_cache

def fib(n):
    if n == 1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)


#need to do this buttom up, not top down
arr =[0,1]
def fibdyn(n,acc):
    acc[n]=fibdyn(n-1,acc) + fibdyn(n-2,acc)
    return acc[n]

@lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)