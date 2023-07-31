from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write
N, M , R = map(int,input().split())
A = [[] for _ in range(N+1)]
visited = [False]*(N+1)
ans = [0]*(N+1)
for _ in range(M):
    s, e  = map(int,input().split())
    A[s].append(e)
    A[e].append(s)
for i in range(1,N+1):
    A[i].sort(reverse=True)
count =1
q = deque()
q.append((R))
visited[R]=True
while len(q)>0:
    now = q.popleft()
    ans[now]=count
    count+=1
    for i in A[now]:
        if not visited[i]:
            visited[i]=True
            q.append(i)

for i in range(1,N+1):
    print(str(ans[i])+"\n")
