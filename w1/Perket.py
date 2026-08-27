n = int(input())
Ss = []
Bs = []
for _ in range(n):
    s,b = map(int, input().split())
    Ss.append(s)
    Bs.append(b)

min_val = abs(Ss[0] - Bs[0])


for k in range(1,1<<n):
    s = 1
    b = 0
    for i in range(n):
        if (k&(1<<i)):
            s *= Ss[i]
            b += Bs[i]
    if (min_val > abs(s-b)):
       min_val = abs(s-b)

print(min_val)
