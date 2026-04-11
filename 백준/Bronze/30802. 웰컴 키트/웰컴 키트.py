a = int(input())
b = list(map(int, input().split()))
if sum(b)!=a:
    exit

c,d = list(map(int,input().split()))

tt = 0
for i in b:
    if i == 0:
        tt+=0
    elif i % c == 0:
        tt+=i//c
    else:
        tt+=i//c+1
pp= a//d
ppp = a%d
print(tt)
print(pp, ppp)