a = input().upper()
b = list(set(a))
c = []
for i in b:
    c.append(a.count(i))
if c.count(max(c))>1:
    print('?')
else:
    f = c.index(max(c))
    print(b[f])    
    