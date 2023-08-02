N = int(input())
A = list(map(int,input().split()))
visited = [False]*N
ans=[]
ans_val = 0
def dfs(depth):
    global ans_val
    if depth==N:
        temp=0
        for i in range(N-1):
            temp += abs(ans[i]-ans[i+1])
        ans_val = max(ans_val,temp)
        return
    for i in range(N):
        if not visited[i]:
            visited[i]=True
            ans.append(A[i])
            dfs(depth+1)
            ans.pop()
            visited[i]=False

dfs(0)
print(ans_val)