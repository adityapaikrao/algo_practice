from typing import List
from union_find import UnionFind


def is_connected(adj: List[List[int]], n: int, in_degree: List[int], out_degree: List[int]) -> bool:
    """
    Checks if all non-isolated nodes belong to the same connected component
    """
    # union all nodes that have an edge between them
    uf = UnionFind(n)
    for src, nbrs in enumerate(adj):
        for nbr in nbrs:
            uf.union(src, nbr)
    
    # check all nodes are either isolated or in the same component
    prev = None
    for node in range(n):
        if in_degree[node] == out_degree[node] == 0: continue # isloated node, skip
        if prev is None:
            prev = node
            continue
        if uf.find(prev) != uf.find(node):
            return False
    
    return True

def check_eulerian(adj: List[List[int]]) -> bool:
    """
    Check if the given graph has a Eulerian Path or not.
    """
    # count indegree & outdegree of each node
    n = len(adj)
    in_degree = [0] * n
    out_degree = [0] * n
    
    for src, nbrs in enumerate(adj):
        for nbr in nbrs:
            in_degree[nbr] += 1
            out_degree[src] += 1
    
    # For a Eulerian path: 
    # 1. All nodes should have indegree=outdegree (Eulerian Circuit) 
    # OR 
    # 2. Exactly one node has outdegree - indegree = 1 and Exactly one node has indegree - outdegree = 1
    # AND
    # 3. All non-isloated nodes should lie in the same connected component
    # i.e (1 OR 2) AND 3
    start_nodes = end_nodes = 0
    for node in range(n):
        match out_degree[node] - in_degree[node]:
            case 1:
                start_nodes += 1
            case -1:
                end_nodes += 1
            case 0:
                continue
            case _:
                return False

    # check condition 1 & 2
    if not (start_nodes == end_nodes == 0 or start_nodes == end_nodes == 1):
        return False

    return is_connected(adj, n, in_degree, out_degree) # check condition 3
    


if __name__ == "__main__":
    adj = [[1], [2], [3, 4], [2], [5], []]
    exists = check_eulerian(adj)
    print(exists)