from queue import PriorityQueue
import sys
input = sys.stdin.readline
N,E = map(int,input().split())
A = [[] for i in range(N+1)]
for _ in range(E):
    s,e,v = map(int,input().split())
    A[s].append((e,v))
    A[e].append((s,v))

v1, v2 = map(int,input().split())
distance1 = [sys.maxsize]*(N+1)
distance2 = [sys.maxsize]*(N+1)
distance1[v1]= 0
q= PriorityQueue()
q.put((0,v1))
while not q.empty():
    value , now = q.get()
    for i,v in A[now]:
        if distance1[i]>distance1[now]+v:
            distance1[i]=distance1[now]+v
            q.put((v,i))

distance2[v2]= 0
q= PriorityQueue()
q.put((0,v2))
while not q.empty():
    value , now = q.get()
    for i,v in A[now]:
        if distance2[i]>distance2[now]+v:
            distance2[i]=distance2[now]+v
            q.put((v,i))

ans = (distance1[v2])+min(distance1[1]+distance2[N],distance1[N]+distance2[1])
if ans >=sys.maxsize:
    print(-1)
else:
    print(ans)



