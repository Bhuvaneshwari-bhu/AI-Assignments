class State:
    def __init__(self, pos):
        self.pos = pos

    def __str__(self):
        return ''.join(self.pos)

    def __hash__(self):
        return hash(''.join(self.pos))

    def __eq__(self, value):
        return self.pos == value.pos

    def goalTest(self):
        return self.pos == ['E', 'E', 'E', '_', 'W', 'W', 'W']

    def moveGen(self):
        children = []
        i = self.pos.index('_')

        def swap(j):
            new = self.pos.copy()
            new[i], new[j] = new[j], new[i]
            children.append(State(new))

        if i > 0 and self.pos[i - 1] == 'W':
            swap(i - 1)
        if i > 1 and self.pos[i - 2] == 'W' and self.pos[i - 1] in ['E', 'W']:
            swap(i - 2)

        if i < len(self.pos) - 1 and self.pos[i + 1] == 'E':
            swap(i + 1)
        if i < len(self.pos) - 2 and self.pos[i + 2] == 'E' and self.pos[i + 1] in ['W', 'E']:
            swap(i + 2)

        return children

def removeSeen(children, OPEN, CLOSE):
    open_nodes = [node for node, _ in OPEN]
    close_nodes = [node for node, _ in CLOSE]
    return [c for c in children if c not in open_nodes and c not in close_nodes]

def reconstruct_path(node_pair, CLOSE):
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

# ------------------ BFS ------------------
def bfs(start):
    OPEN = [(start, None)]
    CLOSE = []

    while OPEN:
        node, parent = OPEN.pop(0)
        if node.goalTest():
            print("\nBFS: Goal Found")
            path = reconstruct_path((node, parent), CLOSE)
            for step in path:
                print("->", step)
            return
        CLOSE.append((node, parent))
        children = node.moveGen()
        new_nodes = removeSeen(children, OPEN, CLOSE)
        for c in new_nodes:
            OPEN = OPEN + [(c, node)]
    print("BFS: No solution found.")

# ------------------ DFS ------------------
def dfs(start):
    OPEN = [(start, None)]
    CLOSE = []

    while OPEN:
        node, parent = OPEN.pop(0)
        if node.goalTest():
            print("\nDFS: Goal Found")
            path = reconstruct_path((node, parent), CLOSE)
            for step in path:
                print("->", step)
            return
        CLOSE.append((node, parent))
        children = node.moveGen()
        new_nodes = removeSeen(children, OPEN, CLOSE)
        for c in new_nodes:
            OPEN = [(c, node)] + OPEN
    print("DFS: No solution found.")

start = State(['W', 'W', 'W', '_', 'E', 'E', 'E'])

print(" BFS:")
bfs(start)

print("\n DFS:")
dfs(start)
