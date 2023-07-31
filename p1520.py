M, N = map(int,input().split())
A = []
dp = [[-1 for j in range(N)] for i in range(M)]
for _ in range(M):
    A.append(list(map(int,input().split())))
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def dfs(x,y):
    if x==M-1 and y ==N-1:
        return 1
    if dp[x][y]!=-1:
        return dp[x][y]
    dp[x][y]=0
    for i in range(4):
        next_x = x+dx[i]
        next_y = y + dy[i]
        if next_x>=0 and next_y>=0 and next_x<M and next_y<N:
            if A[x][y]>A[next_x][next_y]:
                dp[x][y]+=dfs(next_x,next_y)
    
    return dp[x][y]

print(dfs(0,0))
    
