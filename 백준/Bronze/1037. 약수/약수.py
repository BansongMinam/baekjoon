n_number = int(input())
n = list(map(int, input().split()))


if n_number == len(n):
    n.sort() 
    print(n[0] * n[-1])