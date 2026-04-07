a,b = input().split()#숫자에는 슬라이싱 사용 못한다 아
aa = a[::-1]
bb = b[::-1]
if int(aa)>int(bb):
    print(aa)
else:
    print(bb)