# -----------------------------------------
N = 7
R = 6
list = [1,2,3,4,5,6,7]
choose = []

# 재귀함수를 사용한 순열,조합 문제
def combination(index, level):
    # Base Code
    if level == R:
        print(choose)
        return
    
    # Recursive Code
    for i in range(index, N):
        choose.append(list[i])
        combination(i+1, level+1)
        choose.pop()

# -----------------------------------------
# 로또 문제풀이 with 재귀+순열,조합 사용

def lotto(index,level):
    global choose, arr, k

    if level == 6:
        for u in choose:
            print(u, end=" ")
        print()
        return
    
    for i in range(index,k):
        choose.append(arr[i])
        lotto(i+1, level+1)
        choose.pop()

while True:
    choose = []

    # input = list(map(int, input().split()))
    # 위 코드에서 발생하는 TypeError는 input() 함수가 전역 변수로 사용되기 때문입니다.
    # Python의 내장 함수 input()과 동일한 이름의 변수를 사용할 경우, 
    # 이후 코드에서 input()을 호출할 때 함수로 인식되지 않고, 변수로 인식되어 오류가 발생할 수 있습니다.
    # 구체적으로 문제는 input = list(map(int, input().split()))에서 발생합니다. 
    # 여기서 input이라는 변수 이름이 Python의 input() 함수와 이름이 충돌하게 됩니다.
    
    I = list(map(int, input().split()))

    k = I[0]
    arr = I[1:]
    if k == 0:
        break

    # lotto(0,0)
    print()
    
# -----------------------------------------
# 파이썬 라이브러리 사용한 문제풀이
from itertools import combinations

while True:
    I2 = list(map(int, input().split()))
    k = I2[0]
    arr = I2[1:]
    if k == 0:
        break
    for comb in combinations(arr,6):
        
        for u in comb:
            print(u, end=" ")
        print()
    print()
