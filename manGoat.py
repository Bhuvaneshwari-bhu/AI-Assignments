def removeSeen(children,OPEN,CLOSE):
    open_nodes=[node for node,parent in OPEN]
    close_nodes=[node for node,parent in CLOSE]
    new_nodes=[c for c in children if not c in open_nodes and c not in close_nodes]
    return new_nodes
def recopa(node_pair,CLOSE):
    path=[]
    parent_map={}
    for node,parent in CLOSE:
        parent_map[node]=parent
    node,parent=node_pair
    path.append(node)
    while parent is not None:
        path.append(parent)
        parent=parent_map[parent]
    return path
def bfs(start):
    OPEN=[(start,None)]
    CLOSE=[]
    while OPEN:
        node_pair=OPEN.pop(0)
        N,parent=node_pair
        if N.goalTest():
            print("goal is found")
            path=recopa(node_pair,CLOSE)
            for e in path:
                print(f"->{e}")
            return
        else:
            CLOSE.append(node_pair)
            children=N.moveGen()#genrate children a,b,c,d,e
            new_nodes=removeSeen(children,OPEN,CLOSE)# b,d
            new_pairs=[(c,N) for c in new_nodes]#(b,N) (d,N)
            OPEN=OPEN+new_pairs
    return []

class State:
    def __init__(self,man,goat,cab,wolf):#initializing
        self.man=man
        self.goat=goat
        self.cab=cab
        self.wolf=wolf
    def goalTest(self):#checking for goal state
        if self.man=='R' and self.goat=='R' and self.cab=='R' and self.wolf=='R' :
            return True
        else:
            return False
    def isValid(self):
        if self.wolf==self.goat and self.goat != self.man:
            return False
        elif self.cab==self.goat and self.cab != self.man:
            return False
        else: return True
        
    def moveGen(self):#generate children
        children=[]
        newside='R' if self.man=='L' else 'L'#man moving to newside
        items=["wolf","cab","goat",None]
        for e in items:
            if self.man==self.wolf and e=="wolf" :
                child=State(man=newside,goat=self.goat,cab=self.cab,wolf=newside)
            elif self.man==self.goat  and e=="goat":
                child=State(man=newside,goat=newside,cab=self.cab,wolf=self.wolf)
            elif self.man==self.cab and e=="cab":
                child=State(man=newside,goat=self.goat,cab=newside,wolf=self.wolf)
            elif e is None:
                child=State(man=newside,goat=self.goat,cab=self.cab,wolf=self.wolf)
            else: continue #no need to append a child
            if child.isValid():
                children.append(child)
        return children
    def __str__(self):
        return "M:"+self.man+" G:"+self.goat+" W:"+self.wolf+" C:"+self.cab
    def __eq__(self, value):
        if self.man==value.man and self.wolf==value.wolf and self.cab==value.cab and self.goat==value.goat:
            return True
        else: return False
    def __hash__(self):
        return hash(self.man+self.wolf+self.cab+self.goat)
    
start_state=State(man='L',goat='L',cab='L',wolf='L')
bfs(start_state)
# for i in start_state.moveGen():
#     print(i)
#     if i.goalTest(): break