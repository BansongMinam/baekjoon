cup = [1,2,3]
m = int(input())
for i in range(m):
    x, y = map(int,input().split())
    a = cup.index(x)
    b = cup.index(y)
    cup[a], cup[b] = cup[b], cup[a]

print(cup[0])