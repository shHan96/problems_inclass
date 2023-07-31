from collections import Counter
import sys
input = sys.stdin.readline
print = sys.stdout.write
N = int(input())
A = list(map(int,input().split()))
d = Counter(A)
s = []
ans = [-1 for _ in range(N)]
for i,x in enumerate(A):
    if not s:
        s.append(i)
    else:
        while s and d[A[s[-1]]]<d[x]:
            ans[s[-1]]=x
            s.pop()
        s.append(i)
for i in s:
    ans[i]=-1

for i in ans:
    print(str(i)+" ")

         