import sys

input = sys.stdin.readline

N,M = map(int,input().split())
dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

arrayK = [0]
arrayW = [0]

for _ in range(N):
    tempK,tempW = map(int,input().split())
    arrayK.append(tempK)
    arrayW.append(tempW)
   
for i in range(1,N+1):
    for j in range(1,M+1):
        dp[i][j] = dp[i-1][j]
        if j - arrayK[i] >=0 :
            dp[i][j] = max(dp[i][j], (dp[i-1][j-arrayK[i]]) + arrayW[i])
            

print(dp)
print(dp[N][M])
# -----------------------------------------------------------------

# N, K = map(int, input().split())

# W = [0]
# V = [0]

# for _ in range(N):
#     w, v = map(int, input().split())
#     W.append(w)
#     V.append(v)

# dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
# print(dp)

# for n in range(1, N + 1):
#     for k in range(1, K + 1): 
#         dp[n][k] = dp[n - 1][k]
#         if k - W[n] >= 0:
#             dp[n][k] = max(dp[n][k], dp[n - 1][k - W[n]] + V[n])

# print(dp[N][K])

