from itertools import permutations

N = int(input())

numbers = [input().split() for _ in range(N)]
answer = 0

for nums in permutations(range(1,10), 3):
    ok = True
    # print(num)
    for num,strike,ball in numbers:
        currentStrike = 0
        currentBall = 0
        
        for i in range(3):
            if str(nums[i]) == num[i]:
                currentStrike += 1
            elif  str(nums[i]) in num:
                currentBall += 1
        
        if currentStrike != int(strike) or currentBall != int(ball):
            ok = False
            break
    
    if ok:
        answer += 1
            
        

print(answer)

