N = int(input())

infos = [list(map(int,input().split())) for _ in range(N)]

# infos = sorted(infos, key=lambda x : (x[1] * x[2] * x[3], x[1] + x[2] + x[3], x[0]))
infos = sorted(infos, key=lambda x : (x[1] * x[2] * x[3], x[1] + x[2] + x[3], x[0]))

for a,b,c,d in infos[0:3]:
    print(a, end=" ")



