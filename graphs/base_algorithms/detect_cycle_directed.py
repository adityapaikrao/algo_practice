from collections import deque

def detect_cycle_dfs(adj, V):
    visited = [0 for _ in range(V)]

    def dfs(node):
        nonlocal visited, adj
        visited[node] = 1 # mark as currently visiting

        for nbr in adj[node]:
            if visited[nbr] == 1: return True
            elif visited[nbr] == 0 and dfs(nbr): return True
        
        visited[node] = 2 # mark as visited
        return False

    for start_node in range(V):
        if visited[start_node] != 0: continue

        if dfs(start_node): return True
    
    return False


def detect_cycle_bfs(edges, V):
    adj = [[] for _ in range(V)]
    in_degree = [0] * V
    visited = [False for _ in range(V)]

    for u, v in edges:
        adj[u].append(v)
        in_degree[v] += 1
    
    count = 0
    q = deque([])
    for v in range(V):
        if in_degree[v] == 0:
            q.append(v)
    
    while q:
        node = q.popleft()
        count += 1

        for nbr in adj[node]:
            in_degree[nbr] -= 1
            if in_degree[nbr] == 0:
                q.append(nbr)
    
    return count != V


if __name__ == "__main__":
    edges = [[0, 1], [0, 2], [1, 2], [2, 0], [2, 3]]
    V = 4

    adj = [[] for _ in range(V)]

    for u, v in edges:
        adj[u].append(v)
    
    print(f'{detect_cycle_dfs(adj, V)}')
    print(f'{detect_cycle_bfs(edges, V)}')