N = int(input())

# print(result)
[['3', '4'], ['1', '1'], ['1', '-1'], ['2', '2'], ['3', '3']]
['3 4', '1 1', '1 -1', '2 2', '3 3']
[[3, 4], [1, 1], [1, -1], [2, 2], [3, 3]]
dots = [list(map(int, input().split())) for _ in range(N)]
print(dots)
dots = sorted(dots)

for x,y in dots:
    print(x,y, )
    
result = [list(map(int,input().split())) for _ in range(N)]