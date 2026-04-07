def d(n):
    sum_value = n 
    for i in str(n):
        sum_value += int(i)
    return sum_value
a = set()
for i in range(1,10001):
    a.add(d(i))
for j in range(1,10001):
    if j not in a:
        print(j)
        
                
    
    