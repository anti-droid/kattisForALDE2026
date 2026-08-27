n = input()
b = False
for c in n:
    if c == 'b':
        b = not b
        c = '0' if b else '1'
    print(c,end = "")
