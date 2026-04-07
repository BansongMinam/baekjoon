import sys
#N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
n =int(sys.stdin.readline())
n = int(n)
d=[]
for i in range(n):
    a = int(sys.stdin.readline())
    d.append(a)
d.sort()    
for j in d:
    print(j)
    