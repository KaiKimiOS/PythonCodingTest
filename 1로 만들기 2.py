# import sys

# input = sys.stdin.readline

# N = int(input())

# dp = [0] * (N+1)
# prev = [0] * (N+1)

# dp[1] = 0
# dp[2] = 1
# dp[3] = 1
# prev[1] = 0


# for i in range(2,N+1):
#     dp[i] = dp[i-1] + 1
#     prev[i] = i - 1
#     if i % 2 == 0 and dp[i] >  dp[i//2] + 1:
#         dp[i] = dp[i//2] + 1
#         prev[i] = i//2
#     if i % 3 == 0 and dp[i] > dp[i//3] + 1:
#         dp[i] = dp[i//3] + 1
#         prev[i] = i//3


# print(dp[N])
 
# print(N, end=" ")
# tempN = N

# while prev[tempN] != 0:
#     print(prev[tempN], end=" ")
#     tempN = prev[tempN]


import sys

input = sys.stdin.readline

N = int(input())

dp = [0] * (N + 1)
prev = [0] * (N + 1)

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1
    prev[i] = i - 1

    if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i // 2] + 1
        prev[i] = i // 2

    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
        dp[i] = dp[i // 3] + 1
        prev[i] = i // 3

# 최소 연산 횟수 출력
print(dp[N])

# 경로 출력
path = []
while N != 0:
    path.append(N)
    N = prev[N]

print(" ".join(map(str, path)))
