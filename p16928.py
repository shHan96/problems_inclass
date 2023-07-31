from collections import deque
N , M = map(int,input().split())
visited = [[False]*7 for i in range(101)]
d = {}
for i in range(N):
    s,e = map(int,input().split())
    d[s]=e
for i in range(M):
    s,e = map(int,input().split())
    d[s]=e

q = deque()
ans =0
q.append([1,0,0])
visited[1][0]=True
while len(q)>0:
    p,dice,t=q.popleft()
    if p in d:
        p = d[p]
    if p==100:
        ans=t
        break
    for i in range(1,7):
        if p+i <=100 and not visited[p+i][i]:
            visited[p+i][i]=True
            q.append([p+i,i,t+1])


print(ans)