W = 1000
Wp = 10000
P = []
for i in range(int(input())):
    P.append(int(input()))

r1 = set()
r1.add(0)
for w in P:
    r2 = set()
    for x in r1:
        r2.add(x)
        if x+w < W:
            r2.add(x+w)
        else:
            Wp = min(Wp,x+w)
    r1 = r2

Wl = max(r1)
if (W-Wl < Wp-W):
    print(Wl)
else:
    print(Wp)