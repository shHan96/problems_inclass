K, N = map(int,input().split())
A = []
for _ in range(K):
    A.append(int(input()))
ans = []
s =1
e = max(A)
ans =0
while s <= e:
    mid = (s+e)//2
    count =0
    for i in A:
        count+=i//mid
    if count<N:
        e=mid-1
    else:
        ans=max(ans,mid)
        s=mid+1
print(ans)
