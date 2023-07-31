from collections import deque
import sys
def solution(n, edge):
    visited = [False]*(n+1)
    A =[[]for i in range(n+1)]
    for s,e in edge:
        A[s].append(e)
        A[e].append(s)
    distance = [sys.maxsize]*(n+1)
    distance[1]=0
    visited[1]=True
    q=deque()
    q.append(1)
    while len(q)>0:
        now = q.popleft()
        for i in A[now]:
            if not visited[i]:
                visited[i]=True
                distance[i] = min(distance[i],distance[now]+1)
                q.append(i)
    max_value=0
    for i in range(1,n+1):
        if distance[i]==sys.maxsize:
            continue
        else:
            if max_value<distance[i]:
                max_value=distance[i]
    
    answer = distance.count(max_value)
    return answer