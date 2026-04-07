d = []
for i in range(9):
    a=int(input())
    d.append(a)
c = max(d)
v = d.index(c) + 1
print(c,v)