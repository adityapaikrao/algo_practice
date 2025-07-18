def dfs_iterative(start_node, adj):
    dfs = []

    stack = [start_node]
    visited = set()

    while stack:
        node = stack.pop()
        if node in visited: continue

        visited.add(node)
        dfs.append(node)

        for nbr in adj[node]:
            if nbr not in visited:
                stack.append(nbr)
    
    return dfs

def dfs_recursive(start_node, adj):
    global dfs_visited, dfs

    if start_node in dfs_visited: return

    dfs_visited.add(start_node)
    dfs.append(start_node)

    for nbr in adj[start_node]:
        dfs_recursive(nbr, adj)

    return 

if __name__ == "__main__":
    adj = [[2, 3, 1], [0], [0, 4], [0], [2]] # connected, undirected
    print(dfs_iterative(0, adj))

    dfs_visited = set()
    dfs = []

    dfs_recursive(0, adj)

    print(dfs)
