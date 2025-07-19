def tarjans(adj, V):
    """
    1. Initialise ids, low_links and on_stack for all vertices
    2. Start DFS for node:
        - assign low_link = id = value() and put on stack
        - for each nbr: 
            - Do DFS if not visited
            - After DFS for neighbour, if nbr on stack: low_link = min(curr low link, nbr's low link)
        - After all neighbors, if low_link == self id -> this starts SCC:
            - pop elements from stack until node is popped off
            - All popped off elements belong to one SCC
        
        < Rinse and Repeat for each node start node that is unvisited>
    
    Intuition is that the low link points to the smalles id reachable by that node: 
    therefore when we reach a node that has low link equal to its own id => its a start of the SCC 
    and all other nodes currently on stack must be on the same SCC 
    """
    V = len(adj)
    ids = [-1] * V
    low_links = [-1] * V
    on_stack = [False] * V 

    id = 0
    stack = []
    all_scc = []


    def tarjan_dfs(node):
        nonlocal id, low_links, ids, all_scc
        low_links[node] = id
        ids[node] = id
        id += 1

        stack.append(node)
        on_stack[node] = True

        for nbr in adj[node]:
            if ids[nbr] == -1:
                tarjan_dfs(nbr)
            
            if on_stack[nbr]:
                low_links[node] = min(low_links[node], low_links[nbr])
        
        if low_links[node] == ids[node]:
            scc = []
            while True:
                scc_node = stack.pop()
                on_stack[scc_node] = False
                scc.append(scc_node)
                if scc_node == node: break
        
            all_scc.append(scc)
            
    
    for start_node in range(V):
        if ids[start_node] != -1: continue

        tarjan_dfs(start_node)
    
    return len(all_scc)