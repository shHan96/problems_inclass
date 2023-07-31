from collections import deque
import sys
input = sys.stdin.readline
N , M = map(int,input().split())
A =[]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for _ in range(N):
    A.append(list(map(int,list(input().strip()))))

visited = [[[False]*2 for _ in range(M)] for i in range(N)]

q = deque()
q.append((0,0,1,0))
visited[0][0][0]=True
ans =-1
while len(q)>0:
    now_x,now_y,depth,wall = q.popleft()
    if now_x==N-1 and now_y==M-1:
        ans=depth
        break
    for i in range(4):
        next_x = now_x+dx[i]
        next_y = now_y+dy[i]
        
        if next_x>=0 and next_x<N and next_y >=0 and next_y<M:
            if A[next_x][next_y]==0:
                if not visited[next_x][next_y][wall]:
                    visited[next_x][next_y][wall]=True
                    q.append((next_x,next_y,depth+1,wall))
            elif A[next_x][next_y]==1 and wall ==0:
                if not visited[next_x][next_y][1]:
                    visited[next_x][next_y][1]=True
                    q.append((next_x,next_y,depth+1,1))
print(ans)     