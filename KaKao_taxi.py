from queue import PriorityQueue
import sys
def solution(n, s, a, b, fares):
    answer = 0
    distanceA = [sys.maxsize]*(n+1)
    distanceB = [sys.maxsize]*(n+1)
    distanceS = [sys.maxsize]*(n+1)
    
    A = [[] for i in range(n+1)]
    for i,j,v in fares:
        A[i].append((j,v))
        A[j].append((i,v))
    pq =PriorityQueue()
    distanceA[a]=0
    visitedA[a]=True
    pq.put((0,a))
    while pq.qsize()>0:
        v,now = pq.get()
        for i,value in A[now]:
            if distanceA[i]>distanceA[now]+value:
                distanceA[i]=distanceA[now]+value
                pq.put((distanceA[i],i))
    
    pq = PriorityQueue()
    distanceB[b]=0
    pq.put((0,b))
    while pq.qsize()>0:
        v,now = pq.get()
        for i,value in A[now]:
            if distanceB[i]>distanceB[now]+value:
                distanceB[i]=distanceB[now]+value
                pq.put((distanceB[i],i))
    pq = PriorityQueue()
    distanceS[s]=0
   
    pq.put((0,s))
    while pq.qsize()>0:
        v,now = pq.get()
        for i,value in A[now]:
            if distanceS[i]>distanceS[now]+value:
                distanceS[i]=distanceS[now]+value
                pq.put((distanceS[i],i))
    answer = sys.maxsize
    for i in range(1,n+1):
        if distanceS[i]==sys.maxsize or distanceA[i]==sys.maxsize or distanceB[i]==sys.maxsize:
            continue
        answer = min(answer,distanceS[i]+distanceA[i]+distanceB[i])
    return answer

