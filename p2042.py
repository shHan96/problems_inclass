import sys
import math
input = sys.stdin.readline
N, M, K = map(int,input().split())

x = len(bin(N))-2
A = [0]*(int(pow(2,x+1)))
t = int(pow(2,x))
def change(b,c):
    indexb = t+b-1
    temp = A[indexb]
    A[indexb]=c
    while indexb>1:
        A[indexb//2]+=A[t+b-1]-temp
        indexb//=2

def subsum(b,c):
    start = b+t-1
    end = c+t-1
    temp = []
    while start<end:
        if start%2==1:
            temp.append(A[start])
        if end%2==0:
            temp.append(A[end])
        nexts = (start+1)//2
        nexte = (end-1)//2
        start=nexts
        end = nexte
    temp.append(A[start])
    return sum(temp)
for i in range(N):
    A[i+t]=int(input())

for i in range(N):
    temp = t+i
    while temp>1:
        A[temp//2]+=A[t+i]
        temp //=2

for _ in range(M+K):
    a, b, c = map(int,input().split())
    if a==1:
        change(b,c)
    else:
        print(subsum(b,c))


        
    
    


