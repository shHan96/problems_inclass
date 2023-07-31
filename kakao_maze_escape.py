from collections import deque
dx = [1,0,0,-1]
dy = [0,-1,1,0]
dans = ['d','l','r','u']
reverdans=['u','r','l','d']

def solution(n, m, x, y, r, c, k):
    answer = ''
    result =deque()
    gap_x=r-x
    gap_y=c-y
    possible = k-abs(gap_x)-abs(gap_y)
    if possible <0 or possible%2!=0:
        return "impossible"
    if gap_x >0:
        for _ in range(abs(gap_x)):
            result.append('d')
    if gap_y <0:
        for _ in range(abs(gap_y)):
            result.append('l')
    if gap_y >0:
        for _ in range(abs(gap_y)):
            result.append('r')
    if gap_x < 0:
         for _ in range(abs(gap_y)):
            result.append('u')
    rever=[]

    for  i in range(possible//2):
        for j in range(4):
            temp_x = r+dx[j]
            temp_y = c+dy[j]
            if temp_x>0 and temp_x<=n and temp_y>0 and temp_y<=m:
                r= temp_x
                c = temp_y
                if ord(dans[j])<=ord(result[0]):
                    result.appendleft(dans[j])
                else:
                    result.append(dans[j])
                rever.append(reverdans[j])
                break
    rever.sort()
    for i in rever:
        if ord(i)<=ord(result[0]):
            result.appendleft(i)
        else:
            result.append(i)
                
    answer=''.join(result)
    return answer


print(solution(3,4,2,3,3,1,5))
