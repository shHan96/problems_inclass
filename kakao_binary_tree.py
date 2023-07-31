preorder =[]
postorder = []
import sys
sys.setrecursionlimit(10**6)
def solution(nodeinfo:list):
    answer = [[]]
    N = len(nodeinfo)
    newnodeinfo = [(nodeinfo[i][0],nodeinfo[i][1],i+1) for i in range(N)]
    newnodeinfo.sort(key= lambda x : (-x[1],x[0]))
    head = Node(newnodeinfo[0][0],newnodeinfo[0][1],newnodeinfo[0][2])
    for i in range(1,N):
        position(head,newnodeinfo[i][0],newnodeinfo[i][1],newnodeinfo[i][2])
    pre(head)
    post(head)
    answer = [preorder,postorder]
    return answer

class Node:
    def __init__(self,x,y,v) -> None:
        self.x = x
        self.y = y
        self.v = v
        self.leftnode = None
        self.rightnode = None

def position(Tree:Node,x,y,v):
    if Tree.x>x:
        if Tree.leftnode !=None:
            position(Tree.leftnode,x,y,v)
        else:
            Tree.leftnode = Node(x,y,v)
    else:
        if Tree.rightnode !=None:
            position(Tree.rightnode,x,y,v)
        else:
            Tree.rightnode = Node(x,y,v)

def post(Tree:Node):
    global postorder
    if Tree is None:
        return
    post(Tree.leftnode)
    post(Tree.rightnode)
    postorder.append(Tree.v)

def pre(Tree:Node):
    global preorder
    if Tree is None:
        return
    preorder.append(Tree.v)
    pre(Tree.leftnode)
    pre(Tree.rightnode)

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))