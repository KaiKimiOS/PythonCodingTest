# import sys

# input = sys.stdin.readline

# N = int(input())
# arr = [0]
# arr += list(map(int, input().split()))

# dp = [0]  * (N+1)
# dp[1] = 1


# for i in range(2,N+1):
#     answer = 0
#     for j in range(1,i):
        
#         if arr[i] > arr[j]:
#             answer = max(answer, dp[j])
#     dp[i] = answer + 1
    

# print(max(dp))



n = int(input())
A = list(map(int,input().split()))
d = [1]*n

for i in range(1,n):
    for j in range(i):
        
        if A[j]<A[i]:
            d[i] = max(d[i],d[j]+1)
            
print(max(d))
