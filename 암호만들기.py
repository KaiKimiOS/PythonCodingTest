# 최소 1개의 모음, 최소 2개의 자음

vows = [ "a", "e", "i", "o", "u"] 
answer = []


def isPossible():
    global vow, answer, L, C
     
    vow = 0

    for c in answer:
        vow += (c in vows)
    con = L - vow
    
    return (vow >= 1 and con >= 2)


def createPassword(index, next):
    global vow, answer, L, C
    
    
    if next == L:
        if isPossible():
            print(''.join(answer))
        return
    
    for i in range(index,C):
        answer.append(arr[i])
        createPassword(i+1, next+1)
        answer.pop()
    
createPassword(0,0)



# -------------------------------------------------

from itertools import combinations

vows2 = [ "a", "e", "i", "o", "u"] 

def isPossible1(word):
    global answer, L, C
     
    vow = 0

    for w in word:
        vow += (w in vows2)
    con = L - vow
    
    return (vow >= 1 and con >= 2)

L, C = map(int, input().split())
arr = input().split()

arr.sort()



for word in combinations(arr, L):
   
    if isPossible1(word):
       	print(''.join(word))
        