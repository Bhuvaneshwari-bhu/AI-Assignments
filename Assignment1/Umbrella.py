#Amogh,Ameya and their grandparents have to cross a bridge over the river within one hour to catch a train.It is raining and they have only one unbrella which can be shared by two people .Assuming that no one wants to get wet ,how can they cross in an hour or less?
#Amogh can cross the bridge in 5 min ,Ameya in 10,Their grandmother in 20 and their grand Father in 25.Design a search algorithm

class State:
    def __init__(self, ameya, amogh, gm, gf, umb, time):
        self.ameya = ameya
        self.amogh = amogh
        self.gm = gm
        self.gf = gf
        self.umb = umb
        self.time = time

    def goalTest(self):
        return self.ameya == 'R' and self.amogh == 'R' and self.gm == 'R' and self.gf == 'R'

    def __eq__(self, other):
        return (self.ameya == other.ameya and self.amogh == other.amogh and
                self.gm == other.gm and self.gf == other.gf and self.umb == other.umb and self.time == other.time)

    def __hash__(self):
        return hash((self.ameya, self.amogh, self.gm, self.gf, self.umb, self.time))

    def __str__(self):
        return f"Ameya:{self.ameya} Amogh:{self.amogh} GM:{self.gm} GF:{self.gf} Umbrella:{self.umb} Time:{self.time}"

    def moveGen(self):
        people = [
            ("ameya", 10, self.ameya),
            ("amogh", 5, self.amogh),
            ("gm", 20, self.gm),
            ("gf", 25, self.gf)
        ]
        children = []

        if self.umb == 'L':
            # Send two from L to R
            for i in range(len(people)):
                for j in range(i + 1, len(people)):
                    p1, t1, side1 = people[i]
                    p2, t2, side2 = people[j]
                    if side1 == 'L' and side2 == 'L':
                        ameya = 'R' if p1 == 'ameya' or p2 == 'ameya' else self.ameya
                        amogh = 'R' if p1 == 'amogh' or p2 == 'amogh' else self.amogh
                        gm = 'R' if p1 == 'gm' or p2 == 'gm' else self.gm
                        gf = 'R' if p1 == 'gf' or p2 == 'gf' else self.gf
                        time = self.time + max(t1, t2)
                        if time <= 60:
                            children.append(State(ameya, amogh, gm, gf, 'R', time))
        else:
            # Return one from R to L
            for p, t, side in people:
                if side == 'R':
                    ameya = 'L' if p == 'ameya' else self.ameya
                    amogh = 'L' if p == 'amogh' else self.amogh
                    gm = 'L' if p == 'gm' else self.gm
                    gf = 'L' if p == 'gf' else self.gf
                    time = self.time + t
                    if time <= 60:
                        children.append(State(ameya, amogh, gm, gf, 'L', time))
        return children


def removeSeen(children, OPEN, CLOSE):
    open_nodes = [node for node, _ in OPEN]
    close_nodes = [node for node, _ in CLOSE]
    return [c for c in children if c not in open_nodes and c not in close_nodes]


def recopa(node_pair, CLOSE):
    path = []
    parent_map = {}
    for node, parent in CLOSE:
        parent_map[node] = parent
    node, parent = node_pair
    while parent is not None:
        path.append(node)
        node, parent = parent, parent_map[parent]
    path.append(node)
    return path[::-1]


def bfs(start):
    OPEN = [(start, None)]
    CLOSE = []

    while OPEN:
        node_pair = OPEN.pop(0)
        node, parent = node_pair

        if node.goalTest():
            print("Goal Found!")
            path = recopa(node_pair, CLOSE)
            for p in path:
                print("->", p)
            return

        CLOSE.append(node_pair)
        children = node.moveGen()
        new_nodes = removeSeen(children, OPEN, CLOSE)
        new_pairs = [(c, node) for c in new_nodes]
        OPEN=OPEN+new_pairs

    print("No solution found.")

def dfs(start):
    OPEN = [(start, None)]
    CLOSE = []

    while OPEN:
        node_pair = OPEN.pop(0)
        node, parent = node_pair

        if node.goalTest():
            print("Goal Found!")
            path = recopa(node_pair, CLOSE)
            for p in path:
                print("->", p)
            return

        CLOSE.append(node_pair)
        children = node.moveGen()
        new_nodes = removeSeen(children, OPEN, CLOSE)
        new_pairs = [(c, node) for c in new_nodes]
        OPEN=new_pairs+OPEN

    print("No solution found.")
start_state = State('L', 'L', 'L', 'L', 'L', 0)
print("BFS:")
bfs(start_state)
print("DFS:")
dfs(start_state)


# BFS:
# Goal Found!
# -> Ameya:L Amogh:L GM:L GF:L Umbrella:L Time:0
# -> Ameya:R Amogh:R GM:L GF:L Umbrella:R Time:10
# -> Ameya:L Amogh:R GM:L GF:L Umbrella:L Time:20
# -> Ameya:L Amogh:R GM:R GF:R Umbrella:R Time:45
# -> Ameya:L Amogh:L GM:R GF:R Umbrella:L Time:50
# -> Ameya:R Amogh:R GM:R GF:R Umbrella:R Time:60
# DFS:
# Goal Found!
# -> Ameya:L Amogh:L GM:L GF:L Umbrella:L Time:0
# -> Ameya:R Amogh:R GM:L GF:L Umbrella:R Time:10
# -> Ameya:L Amogh:R GM:L GF:L Umbrella:L Time:20
# -> Ameya:L Amogh:R GM:R GF:R Umbrella:R Time:45
# -> Ameya:L Amogh:L GM:R GF:R Umbrella:L Time:50
# -> Ameya:R Amogh:R GM:R GF:R Umbrella:R Time: