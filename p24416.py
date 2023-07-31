dp = [0]*41
dp[1]=1
dp[2]=1
def fibo(N):
    if dp[N]!=0:
        return dp[N]
    dp[N] = fibo(N-1)+fibo(N-2)
    return dp[N] 
  

N = int(input())
print(fibo(N),N-2)