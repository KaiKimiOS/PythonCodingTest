def psum(sy,sx,ey,ex):
    global psumArray
    return psumArray[ey][ex] - (psumArray[ey][sx-1] + psumArray[sy-1][ex] - psumArray[sy-1][sx-1])


N = 4
M = 5

arr = [
	[0, 0, 0, 0, 0, 0],
	[0, 10, 10, 3, 8, 4],
	[0, 9, 8, 4, 1, 10],
	[0, 7, 6, 5, 6, 5],
	[0, 2, 6, 6, 4, 10]
]

psumArray = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

for i in range(1,N+1):
    for j in range(1, M +1):
        psumArray[i][j] = (psumArray[i-1][j] + psumArray[i][j-1] - psumArray[i-1][j-1]) + arr[i][j]
    
print(psum(3,3,4,5))



