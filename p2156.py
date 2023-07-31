N = int(input())
A = [0]
dp=[0 for _ in range(N+1)]
for _ in range(N):
    A.append(int(input()))
dp[1]= A[1]
if N>=2:
    dp[2]=A[1]+A[2]

for i in range(3,N+1):
    dp[i]=max(dp[i-2]+A[i],A[i]+A[i-1]+dp[i-3],dp[i-1])

print(dp[N])