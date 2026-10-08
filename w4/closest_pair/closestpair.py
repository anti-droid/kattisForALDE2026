import cmath
#sys.setrecursionlimit(n)

n = int(input())

l = []
for _ in range(n):
    x,y = map(float,input().split())
    l.append(complex(x,y))

def exhCP(P, start, end):
    n = end-start
    min_a = P[start]
    min_b = P[start+1]
    min_val = abs(min_a-min_b)
    for i in range(start, start+n):
        for j in range(i+1,start+n):
            loc_min = abs(P[i]-P[j])
            if loc_min < min_val:
                min_a = P[i]
                min_b = P[j]
                min_val = loc_min
    return (min_a,min_b), min_val


def split(L, start, end, real, mid):
    left = []
    right = []
    middle = []

    if real:
        pivot = L[mid].real
        for i in range(start,end):
            if L[i].real < pivot:
                left.append(L[i])
            elif L[i].real == pivot:
                middle.append(L[i])
            else: 
                right.append(L[i])
    else:
        pivot = L[mid].imag
        for i in range(start,end):
            if L[i].imag < pivot:
                left.append(L[i])
            elif L[i].imag == pivot:
                middle.append(L[i])
            else: 
                right.append(L[i])

    for i in range(len(left)):
        L[start+i] = left[i]
    s1 = start+len(left)
    for i in range(len(middle)):
        L[s1+i] = middle[i]
    s2 = s1+len(middle)
    for i in range(len(right)):
        L[s2+i] = right[i]

    if s1 > mid:
        split(L,start,s1,real,mid)
    elif s2 < mid:
        split(L,s2,end,real,mid)
    
def cp(P,start, end, real):
    n = end-start
    if n <= 3: #kan være 2 eller 3
        return exhCP(P, start, end)
    mid = start + (end-start)//2
    split(P,start, end, real, mid)
    l, dl = cp(P, start, mid, not real)
    r, dr = cp(P, mid+1, end, not real)
    d = min(dl,dr)
    p = r
    if (dl < dr):
        p = l
    S = []
    for i in P:
        if real:
            if i.real-x < d:
                S.append(i)
        else:
            if i.imag-x < d:
                S.append(i)
    real = not real
    if real:
        S.sort(key= lambda x: x.real)
    else: 
        S.sort(key= lambda x: x.imag)
    s, sd = exhCP(S,0,len(S))
    if sd<d:
        return s,sd
    else:
        return p,d
    


(a,b),d = cp(l, 0, len(l), True)
print(a.real, a.imag)
print(b.real, b.imag)