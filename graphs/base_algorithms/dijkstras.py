import heapq

def Dijkstras(adj, V, src):
    """
    Time complexity: O(E * log E) popped at most E times with E entries in heap in worst case 
    + O(E * log E) every edge is checked for each node and added back to heap
    = O (E log E)

    if decrease-key operation in heap:
    O(V * log V) + O(E * log V)
    if fibonacci heap: O(V * log V) + O(E)
    """
    pq = []

    pq.append((0, src)) # dist, node
    visited = [False] * V
    dist = [float('inf')] * V
    dist[src] = 0

    while pq:
        curr_dist, node = heapq.heappop(pq) # pop from heap 
        if visited[node]: continue

        visited[node] = True

        for nbr, weight in adj[node]:
            if curr_dist + weight < dist[nbr]:
                dist[nbr] = curr_dist + weight
                heapq.heappush(pq, (dist[nbr], nbr)) # should ideally be decrease-key operation
    
    return dist





