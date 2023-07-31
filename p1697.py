import sys
from queue import PriorityQueue
N , K = map(int,input().split())

distance= [sys.maxsize]*(100001)


q = PriorityQueue()
q.put((0,N))
distance[N]=0

while not q.empty():
    v,now = q.get()
    for i in (now-1,now+1,now*2):
        if i >=0 and i <=100000:
            if distance[i]>distance[now]+1:
                distance[i]=distance[now]+1
                q.put((distance[i],i))

print(distance[K])
