import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
A = [[] for x in range(N+1)]
visited = [False]*(N+1)
ans=0
count=-1
def dfs(node):
    global count
    visited[node]=True
    count+=1
    for i in A[node]:
        if not visited[i]:
            dfs(i)

for i in range(M):
    s, e =map(int,input().split())
    A[s].append(e)
    A[e].append(s)

dfs(1)
print(count)