N = int(input())
check = [False] * N
answer = []
lst = [1,2,3,4,5,6,7,8]

def all(level):
    if level == N:
        for i in answer:
            print(i, end=" ")
        print()
        return
    
    for i in range(0,N):
        
        if check[i] == True:
            continue
        
        check[i] = True
        answer.append(lst[i])
        
        all(level+1)
        check[i] = False
        answer.pop()
        
        
# all(0)

from itertools import permutations

for p in permutations(range(1, N+1)):
    print(" ".join(map(str,p)))