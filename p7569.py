from collections import deque
import sys
from collections import deque
import sys
input = sys.stdin.readline
M , N, H= map(int,input().split())
visited = [[[False]*M for _ in range(N)] for i in range(H)]

A= []
dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
for i in range(H):
    temp_N=[]
    for j in range(N):
        temp = list(map(int,input().split()))
        temp_N.append(temp)
    A.append(temp_N)
q = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if A[i][j][k]==1:
                visited[i][j][k]=True
                q.append((i,j,k,0))
ans =0
while len(q)>0:
    now_z,now_x,now_y,depth = q.popleft()
    ans = max(ans,depth)
    for i in range(6):
        next_x = now_x+dx[i]
        next_y = now_y+dy[i]
        next_z = now_z+dz[i]
        if next_x>=0 and next_x<N and next_y>=0 and next_y<M and next_z>=0 and next_z<H and A[next_z][next_x][next_y]!=-1:
            if not visited[next_z][next_x][next_y]:
                visited[next_z][next_x][next_y]=True
                A[next_z][next_x][next_y]=1
                q.append((next_z,next_x,next_y,depth+1))

flag = True
for i in range(H):
    for j in range(N):
        for k in range(M):
            if A[i][j][k]==0:
                flag = False
                break
        if flag==False:
            break
    if flag==False:
        break
if flag:
    print(ans)
else:
    print(-1)



