N,M  = list(map(int, input().split()))

arr = list(map(int, input().split()))

answer = []

pos = []
neg = []

for i in arr:
    if i > 0:
        pos.append(i)
    else:
        neg.append(-i)
        
sorted1 = sorted(pos)[::-1]
sorted2 = sorted(neg)[::-1]

for i in sorted1[::M]:
    answer.append(i)
    
for j in sorted2[::M]:
    answer.append(j)
    
print( (2 * sum(answer)) - max(answer))
