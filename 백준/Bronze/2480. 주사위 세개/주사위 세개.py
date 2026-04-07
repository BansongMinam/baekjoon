a, b, c = map(int,input().split())
d = 0 
if a == b == c:
    
    d = 10000 + a * 1000
    print(d)
elif a==b or b==c or c==a:
    if a == b:
        d = 1000+100*a
        print(d)
    elif b==c:
        d = 1000+100*b
        print(d)
    elif c ==a:
        d =  1000+100*c
        print(d)
else:
    print(max(a,b,c)*100)            
    