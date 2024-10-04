import sys

input = sys.stdin.readline


N,M = map(int,input().split())

chess1 = [[" " for _ in range(8)] for _ in range(8)]
chess2 = [[" " for _ in range(8)] for _ in range(8)]

board = [input() for _ in range(N)]

answer = int(1e12)
def getmin(sy, sx):
    global board, chess1, chess2
    case1 = case2 = 0
   
    for i in range(8):
        for j in range(8):
            case1 += (board[sy + i][sx + j] != chess1[i][j])
            case2 += (board[sy + i][sx + j] != chess2[i][j])
            
    print(case1,case2)
    return min(case1, case2)  

for i in range(0,8):
    for j in range(0,8):
        if (i+j) % 2 == 0 :
            chess1[i][j] = "W"
            chess2[i][j] = "B"
        else: 
            chess1[i][j] = "B"
            chess2[i][j] = "W"


for i in range(N):
    for j in range(M):
        if (i + 7 >= N) or (j + 7 >= M): 
            continue
        answer = min(answer, getmin(i,j))
    

print(answer)
        