T = int(input())
import sys
input = sys.stdin.readline
for _ in range(T):
    N = int(input())
    A = list(map(int,input().split()))
    S = [0]*(N+1)
    for i in range(1,N+1):
        S[i]=A[i-1]+S[i-1]
    dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for i in range(1,N+1):
        for j in range(1,N-i+1):
            dp[j][j+i]=sys.maxsize
            for k in range(j,i+j):
                dp[j][i+j]=min(dp[j][i+j],dp[j][k]+dp[k+1][i+j]+S[i+j]-S[j-1])
    print(dp[1][N])

