from collections import deque

def bfs(adj, start_node):
    q = deque([start_node])
    bfs = []
    visited = set()

    while q:
        node = q.popleft()
        if node in visited: continue

        visited.add(node)
        bfs.append(node)

        for nbr in adj[node]:
            if nbr not in visited:
                q.append(nbr)
    
    return bfs

if __name__ == "__main__":
    adj = [[2, 3, 1], [0], [0, 4], [0], [2]] # connected, undirected
    print(bfs(adj, 0))
