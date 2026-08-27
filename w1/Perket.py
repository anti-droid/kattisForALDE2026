n = int(input())
W = []
for _ in range(n):
    W.append(tuple(map(int, input().split())))
min_val = abs(W[0][0] - W[0][1])

for k in range(1,1<<n):
    w = (1,0)
    for i in range(n):
        if (k&(1<<i)):
            w = (w[0] * W[i][0],w[1] + W[i][1])
    t = abs(w[0]-w[1])
    if (min_val > t):
       min_val = t

print(min_val)
