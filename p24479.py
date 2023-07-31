import sys
input = sys.stdin.readline
print = sys.stdout.write
sys.setrecursionlimit(10**6)
N,M,R = map(int,input().split())
visited = [False]*(N+1)
A = [[] for _ in range(N+1)]
ans = [0]*(N+1)
count =1
for _ in range(M):
    s,e = map(int,input().split())
    A[s].append(e)
    A[e].append(s)

for i in range(1,N+1):
    A[i].sort()

def dfs(node):
    global count
    ans[node]=count
    count+=1
    visited[node]=True
    for i in A[node]:
        if not visited[i]:
            dfs(i)

dfs(R)
for i in range(1,N+1):
    print(str(ans[i])+"\n")