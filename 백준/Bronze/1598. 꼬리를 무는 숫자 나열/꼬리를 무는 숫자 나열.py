a, b = map(int, input().split())


x1, y1 = (a - 1) // 4, (a - 1) % 4
x2, y2 = (b - 1) // 4, (b - 1) % 4

result = abs(x1 - x2) + abs(y1 - y2)
print(result)