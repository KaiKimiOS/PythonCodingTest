N = 6
f = [0] * (N + 1)  # DP Table

# 1 ≤ i ≤ 4 인 경우 (예외처리)
f[1] = 1
f[2] = 2
f[3] = 1
f[4] = 1

# 5 ≤ i ≤ N 인 경우 (반복문 이용)
for i in range(5, N + 1):
    f[i] = min(f[i - 1], f[i - 3], f[i - 4]) + 1
    

print(f[N])
