a = int(input())

for i in range(a):
    # 1. 공백: 0, 1, 2, 3... 순서로 늘어남
    for j in range(i):
        print(' ', end='')
    
    # 2. 별: (2*a - 1)에서 시작해서 2개씩 줄어듦
    for k in range(2 * (a - i) - 1):
        print('*', end='')
        
    print()