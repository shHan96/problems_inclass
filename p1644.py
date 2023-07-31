N = int(input())
D = [False]*(N+1)
primes = []
for i in range(2,N+1):
    if not D[i]:
        primes.append(i)
        for j in range(i+i,N+1,i):
            D[j]=True
s = 0
e = 0
ans = 0
if not primes:
    print(0)
    exit()
now_sum =primes[0]
while True:
    if N>now_sum:
        e+=1
        if(len(primes)==e):
            break
        now_sum+=primes[e]
    elif N<now_sum:
        now_sum-=primes[s]
        s+=1
    else:
        ans+=1
        now_sum-=primes[s]
        s+=1

print(ans)
        
