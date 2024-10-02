N = int(input())
arr = [[0,0,0]]
arr += [list(map(int, input().split())) for _ in range(N)]

dp = [[-1,-1,-1] for _ in range(N+1)]


dp[1][0] = arr[1][0]
dp[1][1] = arr[1][1]
dp[1][2] = arr[1][2]

for i in range(2,N+1):
    dp[i][0] =  arr[i][0] +  min(dp[i-1][1], dp[i-1][2])
    dp[i][1] =  arr[i][1] +  min(dp[i-1][0], dp[i-1][2])
    dp[i][2] =  arr[i][2] +  min(dp[i-1][0], dp[i-1][1])
    

print(min(dp[N]))
print(min(dp[N][0], dp[N][1], dp[N][2]))
[[-1, -1, -1], 
 [26, 40, 83], 
 [89, 86, 83], 
 [96, 172, 185]]