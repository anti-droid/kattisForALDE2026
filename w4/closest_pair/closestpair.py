import cmath

n = int(input())

l = []
for _ in range(n):
    x,y = map(float,input().split())
    l.append(complex(x,y))


min_a = l[0]
min_b = l[1]
min_val = abs(l[0]-l[1])
for i in range(n):
    for j in range(i+1,n):
        loc_min = abs(l[i]-l[j])
        if loc_min < min_val:
            min_a = l[i]
            min_b = l[j]
            min_val = loc_min

print(min_a.real, min_a.imag)
print(min_b.real, min_b.imag)