def kosaraju(adj, V):
    # Get post ordering for vertices
    visited = [False] * V
    post_order = []

    def dfs_recursive(node):
        nonlocal visited, post_order
        visited[node] = True

        for nbr in adj[node]:
            if not visited[nbr]: dfs_recursive(nbr)
        
        post_order.append(node)
        return

    for start_node in range(V):
        if visited[start_node]: continue

        dfs_recursive(start_node)
    
    # Reverse Graph Edges
    adj_reversed = [[] for _ in range(V)]
    for u in range(V):
        for v in adj[u]:
            adj_reversed[v].append(u)
    
    # Get SCCs
    all_scc = []
    traversal_order = post_order[::-1] # reverse order of post order
    visited = [False] * V
    for start_node in traversal_order:
        if visited[start_node]: continue

        scc = []
        stack = [start_node]
        while stack:
            node = stack.pop()
            scc.append(node)
            visited[node] = True

            for nbr in adj_reversed[node]:
                if not visited[nbr]: stack.append(nbr)
        
        all_scc.append(scc)
    
    return all_scc


