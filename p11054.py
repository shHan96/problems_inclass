N = int(input())
A = list(map(int,input().split()))
dp = [[1]*2 for i in range(N)]


for i in range(1,N):
    for j in range(1,i+1):
        if A[i]>A[i-j]:
            dp[i][0]=max(dp[i][0],dp[i-j][0]+1)
        elif A[i]<A[i-j]:
            dp[i][1]=max(dp[i][1],dp[i-j][1]+1,dp[i-j][0]+1)
        else:
            dp[i][0]=max(dp[i][0],dp[i-j][0])
            dp[i][1]=max(dp[i][1],dp[i-j][1])
ans= 0
for i in range(N):
    ans = max(ans,max(dp[i]))
print(ans)
