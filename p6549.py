import sys
input = sys.stdin.readline
def divide(heights):
    N = len(heights)
    if N ==1: return heights[0]
    mid = N//2
    left_h = divide(heights[:mid])
    right_h = divide(heights[mid:])
    l = mid-1
    r = mid
    under_w = 2
    min_h = min(heights[l],heights[r])
    max_area = under_w*min_h

    while 0 <=l and r<=N-1:
        lh = heights[l-1] if l>=1 else 0
        rh = heights[r+1] if r < N-1 else 0
        min_h = min(min_h,lh) if lh> rh else min(min_h,rh)
        if lh > rh: l-=1
        else: r+=1
        under_w +=1
        max_area = max(max_area,under_w * min_h)

    return max(left_h,right_h,max_area)


while True:
    A = list(map(int,input().rstrip().split()))
    if len(A)==1 and A[0]==0:
        break
    print(divide(A))
