for _ in range(3):
    n = int(input())
    b = 0
    for i in range(n):
        a = int(input())
        b += a
    
    if b == 0:
        print(0)
    elif b > 0:
        print('+')
    else:
        print('-')