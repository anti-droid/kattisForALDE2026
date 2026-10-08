import random as r
m = 10_000

n = int(input())
print(n)
for i in range(n):
    print(r.random()*m, r.random()*m)