from check_eulerian_path import check_eulerian
from typing import List, Tuple

def find_eulerian_path(adj: List[List[int]]) -> Tuple[List[int], bool]:
    """
    Get an Eulerian Path from the given graph
    """
    if not check_eulerian(adj):
        return [], False

    # count indegree & outdegree of each node
    n = len(adj)
    in_degree = [0] * n
    out_degree = [0] * n
    
    for src, nbrs in enumerate(adj):
        for nbr in nbrs:
            in_degree[nbr] += 1
            out_degree[src] += 1
    
    # Find the start node
    start_node = next((node for node in range(n) if out_degree[node] - in_degree[node] == 1), 
                      next(node for node in range(n) if out_degree[node] > 0)
                )
    
    post_order = []
    stack = [start_node]

    next_node = [0] * n # track the next neighbor to visit for each node
    while stack:
        curr_node = stack[-1]
        if next_node[curr_node] < len(adj[curr_node]):
            nbr = adj[curr_node][next_node[curr_node]]
            next_node[curr_node] += 1
            stack.append(nbr)   
        else:
            post_order.append(stack.pop()) 

    return post_order[::-1], True
    


if __name__ == "__main__":
    adj = [[1], [2], [3, 4], [2], [5], []]
    path, exists = find_eulerian_path(adj)
    print(path, exists)