d = []
for i in range(5):
    a = map(int, input().split())
    d.append(sum(a))

wc = max(d)
wn = d.index(wc) + 1  
print(wn, wc)