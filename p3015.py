import sys
input = sys.stdin.readline
N = int(input())
stack = []
A = []
D = {}
for _ in range(N):
    A.append(int(input()))
ans =0
for i in range(len(A)):

    if not stack:
        stack.append(A[i])
        D[A[i]]=1
        continue
    if stack[-1]>A[i]:
        D[A[i]]=1
        ans+=1
        stack.append(A[i])
    elif stack[-1]==A[i]:
        ans+=D[A[i]]
        if len(stack)>1:
            ans+=1
        D[A[i]]+=1
    else: 
        while stack and stack[-1]<A[i]:
            ans+=D[stack[-1]]
            D[stack[-1]]=0
            stack.pop()
        if not stack:
            D[A[i]]=1
            stack.append(A[i])
        elif stack[-1]==A[i]:
            ans+=D[A[i]]
            if len(stack)>1:
                ans+=1
            D[A[i]]+=1
        else: 
            ans+=1
            D[A[i]]=1
            stack.append(A[i])
        
print(ans)