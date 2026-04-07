a,b,c = map(int,input().split())
d = int(input())
t = a*3600 + b *60 + c + d
t %= 86400 

a = t // 3600
b = (t % 3600) // 60
c = t % 60

print(a, b, c)