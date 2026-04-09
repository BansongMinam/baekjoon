n = int(input())
for i in range(n):
    for j in range(n):
        print("@"*5,end='')
    print()
for i in range(n):
    print("@"*n+"   "*n+"@"*n)
    print("@"*n+"   "*n+"@"*n)
    print("@"*n+"   "*n+"@"*n)
for i in range(n):
    for j in range(n):
        print("@"*5,end='')
    print()

