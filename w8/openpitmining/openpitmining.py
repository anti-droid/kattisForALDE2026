n = int(input())

maxx = 0
s = 0
t = n+1
G = {}
G[s] = {}
G[t] = {}
P = [0]
for i in range(1,n+1):
    l = list(map(int,input().split()))
    v = l[0]
    c = l[1]
    e = l[2:]
    G[i] = {}
    p = v-c
    if p > 0: # vi ignorere profit på 0
        G[s][i]= p
        G[i][s]= 0
    elif p < 0:
        G[i][t] = -p
        G[t][i] = 0
    P.append(e)
    maxx += abs(p)

for i in range(1,n+1):
    e = P[i]
    for j in range(e[0]):
        G[e[j+1]][i] = maxx
        G[i][e[j+1]] = 0

def dfs(G, seen, s, t):
    if s == t:
        return True, [s],maxx
    if s in seen:
        return False, [],maxx
    seen.add(s)
    for u in G[s]:
        if G[s][u] == 0:
            continue
        b,v,c = dfs(G,seen,u,t)
        if b:
            v.append(s)
            return b, v, min(c,G[s][u])
    return False, [], maxx

def FFflow(G,s,t):
    res = 0
    while(True):
        b,v,c = dfs(G,set(),s,t)
        if not b:
            break
        res += c
        #update the flow for an augmented path
        for i in range(1,len(v)):
            G[v[i]][v[i-1]] -= c
            G[v[i-1]][v[i]] += c
    #look through the graph an generate the output
    #hard to do in less than n^2
    # hvordan kender vi foreskel på 0 i backwards og farwards?
    return res

res = set()

flow = FFflow(G,s,t)

profit = 0
for k in G[0]:
    profit += G[0][k]
print(profit)