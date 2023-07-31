S = input().rstrip()
bom = input().rstrip()
stack = []
for i in S:
    stack.append(i)
    if len(stack)>=len(bom):
        flag = True
        for j in range(len(stack)-len(bom),len(stack)):
            if stack[j]!=bom[j-len(stack)+len(bom)]:
                flag=False
                break
        if (flag):
            for j in range(len(bom)):
                stack.pop()
if stack:
    print(''.join(stack))
else:
    print("FRULA")