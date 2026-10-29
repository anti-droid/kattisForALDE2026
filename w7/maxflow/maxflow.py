n,m,s,t = map(int,input().split())
G = {}
fw_edge = set()
C = 0

for i in range(m):
    u,v,c = map(int,input().split())
    C+=c
    if (u not in G):
        G[u] = {}
    if (v not in G[u]):
        G[u][v] = 0
    G[u][v] += c

    if (v not in G):
        G[v] = {}
    if (u not in G[v]):
        G[v][u] = 0
    fw_edge.add((u,v))
    
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

print(FFflow(G,s,t))
