N = int(input())
A = []
for _ in range(N):
    s,e = map(int,input().split())
    A.append([s,e])
A.sort()
dp= [1 for i in range(N)]

for i in range(1,N):
    for j in range(1,i+1):
        if A[i][0] > A[i-j][0] and A[i][1]>A[i-j][1]:
            dp[i] = max(dp[i],dp[i-j]+1)
print(N-max(dp))
        