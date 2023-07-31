from collections import deque
import sys
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]


T = int(input())

for _ in range(T):
    ans = 0
    M,N , L = map(int,input().split())
    A = [[0 for j in range(M)] for i in range(N)]
    for i in range(L):
        s,e = map(int,input().split())
        A[e][s]=1
    for i in range(N):
        for j in range(M):
            if A[i][j]==1:
                ans+=1
                q = deque()
                q.append((i,j))
                A[i][j]=2
                while len(q)>0:
                    now_x,now_y =q.popleft()
                    for k in range(4):
                        next_x = now_x +dx[k]
                        next_y = now_y + dy[k]
                        if next_x>=0 and next_x<N and next_y>=0 and next_y<M and A[next_x][next_y]==1:
                            A[next_x][next_y] =2
                            q.append((next_x,next_y))
    print(ans)