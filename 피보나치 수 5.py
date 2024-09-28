# Fn = Fn-1 + Fn-2 (n ≥ 2)

n = int(input())
arr = [-1] * (n+2)
arr[0] = 0
arr[1] = 1
cnt = 0

# for i in range(2, n + 1):
#     arr[i] =  arr[i-1] +  arr[i-2]

# print(arr[n])
# print(arr)

def fibo(x):
    global cnt
    
    cnt += 1
    if x == 0:
        return 0
    if x == 1:
        return 1
    return fibo(x-1) +  fibo(x-2)

# print(fibo(n))

def fibo2(x):
    global arr,cnt
    cnt += 1
    
    if arr[x] != -1:
        return arr[x]
    
    arr[x] = fibo2(x-1) +  fibo2(x-2)
    return arr[x]


fibo(n)
# print(fibo2(n))
print(cnt)