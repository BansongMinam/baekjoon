#별5 공백 0
#별4 공백 1
a = int(input())
for i in range(1,a+1):
    for j in range(a+1-i):
        print("*",end='')
    print()
    