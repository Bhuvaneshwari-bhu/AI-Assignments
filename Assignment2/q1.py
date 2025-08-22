def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def get_neighbors(x, y, n):
    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < n:
            yield nx, ny

def best_first_search(grid):
    n = len(grid)
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1,[]
    goal = (n-1,n-1)
    visited = set()
    queue = [((0,0),[(0,0)])]
    while queue:
        queue.sort(key=lambda x: heuristic(x[0],goal))
        (x,y),path = queue.pop(0)
        if (x,y) == goal:
            return len(path),path
        if (x,y) in visited:
            continue
        visited.add((x,y))
        for nx,ny in get_neighbors(x,y,n):
            if grid[nx][ny] == 0 and (nx,ny) not in visited:
                queue.append(((nx,ny),path+[(nx,ny)]))
    return -1,[]

def a_star_search(grid):
    n = len(grid)
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1,[]
    goal = (n-1,n-1)
    g = {(0,0):1}
    queue = [((0,0),[(0,0)],1)]
    while queue:
        queue.sort(key=lambda x: x[2] + heuristic(x[0],goal))
        (x,y),path,cost = queue.pop(0)
        if (x,y) == goal:
            return cost,path
        for nx,ny in get_neighbors(x,y,n):
            if grid[nx][ny] == 0:
                new_cost = cost+1
                if (nx,ny) not in g or new_cost < g[(nx,ny)]:
                    g[(nx,ny)] = new_cost
                    queue.append(((nx,ny),path+[(nx,ny)],new_cost))
    return -1,[]

if __name__=="__main__":
    grids = [
        [[0,1],[1,0]],
        [[0,0,0],[1,1,0],[1,1,0]],
        [[1,0,0],[1,1,0],[1,1,0]]
    ]
    for grid in grids:
        bfs_len,bfs_path = best_first_search(grid)
        if bfs_len==-1:
            print("Best First Search  →  Path length: -1")
        else:
            print(f"Best First Search  →  Path length: {bfs_len}, Path: {bfs_path}")
        astar_len,astar_path = a_star_search(grid)
        if astar_len==-1:
            print("A* Search          →  Path length: -1")
        else:
            print(f"A* Search          →  Path length: {astar_len}, Path: {astar_path}")
        print()

