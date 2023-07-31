import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
dp = [1]*N
dp[0]=1
for i in range(1,N):
    for j in range(1,i+1):
       if (A[i]>A[i-j]):
           dp[i]=max(dp[i],dp[i-j]+1)

print(max(dp))
           
    