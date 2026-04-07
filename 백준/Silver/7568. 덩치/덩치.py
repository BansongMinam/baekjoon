a = int(input())
d = []
for i in range(a):
    h,w = map(int,input().split())
    d.append([h, w])

for i in range(a):
    rank = 1
    for j in range(a):
        if d[i][0] < d[j][0] and d[i][1] < d[j][1]:
            rank+=1
    print(rank, end=" ") 
            