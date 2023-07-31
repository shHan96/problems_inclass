import sys
N , S = map(int,input().split())
A = list(map(int,input().split()))
s=0
e=0
now_sum = A[0]
ans = N+1
while True:
    if now_sum<S:
        e+=1
        if e==N:
            break
        now_sum+=A[e]
        
    else:
        ans = min(ans,e-s+1)
        now_sum-=A[s]
        s+=1

if ans<=N:
    print(ans)
else:
    print(0)