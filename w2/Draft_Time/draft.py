from collections import deque

n, m, k = map(int,input().split())
pref = {}
inpref = {}
U = deque()

for j in range(n):
    T = input().split()
    u = T[0]
    A = {}
    for i in range(1,len(T)):
        A[T[i]] = i
    inpref[u] = A

for j in range(k):
    T = input().split()
    u = T[0]
    q = deque()
    for i in range(1,len(T)):
        q.append(T[i])
    pref[u] = q
    U.append(u) 

S = {}
while (U):
    u = U.popleft()
    w = pref[u].popleft()
    if w not in S: S[w] = [u] 
    elif len(S[w]) < m: S[w].append(u)
    else: 
        for i in range(len(S[w])):
            up = S[w][i]
            if inpref[w][u] < inpref[w][up]:
                S[w][i] = u
                u = up
        U.append(u)

for s in S:
    print(s, *(j for j in S[s]))
