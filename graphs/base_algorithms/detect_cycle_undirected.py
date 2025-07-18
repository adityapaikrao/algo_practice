from collections import deque

def bfs_parent_check(adj, V):
    visited = [False for  _ in range(V)]

    for start_node in range(V):
        if visited[start_node]: continue

        q = deque([(start_node, None)]) # node, parent
        
        while q:
            node, parent = q.popleft()
            if visited[node]: continue

            visited[node] = True
            for nbr in adj[node]:
                if nbr == parent: continue
                elif visited[nbr]: return True
                else:
                    q.append((nbr, node))
    
    return False

def bfs_visiting_check(adj, V):
    visited = [0 for _ in range(V)]

    for start_node in range(V):
        if visited[start_node] != 0: continue

        q = deque([])
        q.append(start_node)
        visited[start_node] = 1

        while q:
            node = q.popleft()
            visited[node] = 2

            for nbr in adj[node]:
                if visited[nbr] == 1: return True
                elif visited[nbr] == 0:
                    q.append(nbr)
                    visited[nbr] = 1
        
    return False


def dfs_parent_check(adj, V):
    visited = [False for _ in range(V)]

    def dfs_helper(node, parent):
        nonlocal visited, adj

        visited[node] = True

        for nbr in adj[node]:
            if nbr ==  parent: continue
            elif visited[nbr]: return True
            elif dfs_helper(nbr, node): return True
    
        return False


    for start_node in range(V):
        if visited[start_node]: continue

        if dfs_helper(start_node, None): return True
    
    return False
        

        


if __name__ == "__main__":
    edges = [[0, 1], [0, 2], [1, 2], [2, 3]] # undirected edges
    V = 4

    adj = [[] for _ in range(V)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    print(f'{bfs_parent_check(adj, V)}')
    print(f'{bfs_visiting_check(adj, V)}')
    print(f'{dfs_parent_check(adj, V)}')