n = int(input())

rev = []
for _ in range(n):
    s,f = map(int,input().split())
    rev.append((f,s))

rev.sort()
max_f = 0
res = 0

for i in rev:
    if i[1] >= max_f:
        max_f = i[0]
        res += 1

print(res)
