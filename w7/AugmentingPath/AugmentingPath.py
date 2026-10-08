n,m,s,t = map(int,input().split())
G = {}

C = 0

for i in range(m):
    u,v,c,f = map(int,input().split())
    C+=max(f,c)
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

b,v,c = dfs(G,set(),s,t)
if b:
    print(c)
    print(*reversed(v))
else:
    print("impossible")