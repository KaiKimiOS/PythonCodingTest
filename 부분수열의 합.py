from itertools import combinations

N,S = list(map(int, input().split()))
M = list(map(int, input().split()))
answer = 0

for i in range(1, N+1):
    for j in combinations(M,i):
        if sum(j) == S:
            answer += 1
            
            
print(answer)