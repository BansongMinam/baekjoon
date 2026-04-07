import sys
input = sys.stdin.readline

k, l = map(int, input().split())

res = 0
for i in range(2, l):
    if k % i == 0:
        res = i
        break

if res == 0:
    print("GOOD")
else:
    print("BAD", res)