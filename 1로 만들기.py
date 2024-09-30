N = int(input())

df = [0] * (N + 1)

df[1] = 0

for i in range(2,N+1):
    df[i] = df[i-1] + 1
    if i % 2 == 0 :
        df[i] = min(df[i],df[i//2] + 1 )
    if i % 3 == 0 :
        df[i] = min(df[i], df[i//3] + 1)
  

print(df[N])

