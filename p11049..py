import sys
input = sys.stdin.readline
N = int(input())
A=[(0,0)]
for _ in range(N):
    r,c = map(int,input().split())
    A.append((r,c))
dp = [[0]*(N+1) for i in range(N+1)]

for i in range(1,N):
    for j in range(1,N-i+1):
        dp[j][i+j]=sys.maxsize
        for k in range(j,j+i):
            dp[j][i+j]=min(dp[j][j+i],dp[j][k]+dp[k+1][i+j]+A[j][0]*A[k][1]*A[i+j][1])

print(dp[1][N])