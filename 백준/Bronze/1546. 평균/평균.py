n = int(input())
c=[]
d = list(map(int,input().split()))[:n]

m=max(d)
for i in range(n):
    c.append(d[i]/m*100)
print((sum(c)/n))
    