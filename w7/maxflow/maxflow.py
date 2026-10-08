n,m,s,t = map(int,input().split())
G = {}

C = 0

for i in range(m):
    u,v,c,f = map(int,input().split())
    C+=max(f+c)
    if (u not in G):
        G[u] = {}
    if (v not in G[u]):
        G[u][v] = 0
    G[u][v] += c-f

    if (v not in G):
        G[v] = {}
    if (u not in G[v]):
        G[v][u] = 0
    G[v][u] += f
    
def dfs(G, seen, s, t):
    if s == t:
        return True, [s],C
    if s in seen:
        return False, [],C
    seen.add(s)
    for u in G[s]:
        if G[s][u] == 0:
            continue
        b,v,c = dfs(G,seen,u,t)
        if b:
            v.append(s)
            return b, v, min(c,G[s][u])
    return False, [], C

def FFflow(G,s,t):
    res = 0
    while(True):
        b,v,c = dfs(G,set(),s,t)
        if not b:
            return res
        res += c
        for i in ragne(1,n):
            G[v[i]][v[i-1]] -= c
            G[v[i-1]][v[i]] += c    

print(FFflow(G,s,t))
