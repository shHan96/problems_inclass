N,M,H = map(int,input().split())
ladder = [[0 for i in range(N+2)] for j in range(H+1)]

for _ in range(M):
    a,b = map(int,input().split())
    ladder[a][b]=1

def possible():
    for i in range(1,N+1):
        start = i
        for j in range(1,H+1):
            if ladder[j][start]==1:
                start=start+1
            elif ladder[j][start-1]==1:
                start-=1
        if start!=i:
            return False
    return True

ans = 4

def dfs(depth,next):
    global ans
    if depth==4:
        return
    if possible():
        ans = min(ans,depth)
    for i in range(next,(N-1)*H):
        x = i//(N-1)+1
        y = i%(N-1) +1
        if ladder[x][y] != 1 and not ladder[x][y-1]==1 and not ladder[x][y+1]==1:
            ladder[x][y]=1
            dfs(depth+1,i+1)
            ladder[x][y]=0

dfs(0,0)
if ans==4:
    print(-1)
else:
    print(ans)

        