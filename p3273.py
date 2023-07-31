N = int(input())
A = list(map(int,input().split()))
X = int(input())

A.sort()
s = 0
e = len(A)-1
ans =0
while s <=e:
    temp = A[s]+A[e]
    if temp==X and s!=e:
        ans+=1
        s+=1
        e-=1
    elif temp<X:
        s+=1
    else:
        e-=1
print(ans)