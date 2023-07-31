import sys
input = sys.stdin.readline
N = int(input())
A =[[sys.maxsize for j in range(N)] for i in range(N)]

for i in range(N):
    temp = list(map(int,input().split()))
    for j in range(N):
        if temp[j]==1:
            A[i][j]=1

for K in range(N):
    for i in range(N):
        for j in range(N):
            if A[i][j]> A[i][K]+A[K][j]:
                A[i][j]=A[i][K]+A[K][j]


for i in range(N):
    for j in range(N):
        if A[i][j]==sys.maxsize:
            print(0,end=' ')
        else:
            print(1,end=' ')
    print()              