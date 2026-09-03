from collections import deque

n,m = map(int,input().split())
f = n/2
pref = {}
inpref = {}
U = deque()

for k in range(n):
    inp = input().split()
    u = inp[0]
    q = deque()
    A = {}
    for i in range(1,len(inp)):
        q.append(inp[i])
        A[inp[i]] = i
    inpref[u] = A
    pref[u] = q
    if k < f: U.append(u)

S = {}
while (len(S) < f):
    u = U.popleft()
    w = pref[u].popleft()
    if w not in S: S[w] = u
    else: 
        up = S[w]
        if inpref[w][u] < inpref[w][up]:
            U.append(up)
            S[w] = u
        else: U.append(u)

for s in S:
    print(s + " " + S[s])
