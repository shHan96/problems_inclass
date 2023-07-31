import sys
N = int(input())
A = list(map(int,input().split()))
A.sort()
answer = []
s = 0
e = N-1
index1=s
index2=e
min_value = sys.maxsize
while s < e:
    temp = A[s]+A[e]
    if min_value>abs(temp):
        min_value=abs(temp)
        index1=s
        index2=e
    
    if temp==0:
        break
    elif temp>0:
        e-=1
    else:
        s+=1
print(A[index1],A[index2])


