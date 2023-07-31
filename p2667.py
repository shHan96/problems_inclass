
from collections import deque
import sys
input = sys. stdin.readline
N = int(input())
A = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    q= deque()
    result =0
    q.append((x,y))
    A[x][y] = 2
    while len(q)>0:
        now_x,now_y =q.popleft()
        result+=1
        for i in range(4):
            next_x = now_x +dx[i]
            next_y = now_y + dy[i]
            if next_x>=0 and next_x<N and next_y>=0 and next_y<N and A[next_x][next_y]==1:
                A[next_x][next_y] =2
                q.append((next_x,next_y))
    return result

    



for _ in range(N):
    A.append(list(map(int,list(input().strip()))))
ans= []
for i in range(N):
    for j in range(N):
        if A[i][j]==1:
            ans.append(bfs(i,j))

ans.sort()
print(len(ans))
for i in ans:
    print(i)




