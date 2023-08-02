N = int(input())

def good(s):
    if len(s)==1:
        return True
    for i in range(len(s)//2):
        if s[-1-i:]==s[-2*(i+1):-i-1]:
            return False
    
    return True

def dfs(depth,ans):
    if depth==N:
        print(ans)
        exit(0)
    
    for i in range(1,4):
        if good(ans+str(i)):
            dfs(depth+1,ans+str(i))

dfs(0,"")

