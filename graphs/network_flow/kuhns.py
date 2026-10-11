"""
Kuhns Algorithm for maximum bipartite matching.

"""

def get_max_matching(num_spots: int, preferences: list[list[int]]):
    V = len(preferences)
    if V > num_spots:
        return False, []

    def dfs(node, visited):
        for pref in preferences[node]:
            if pref in visited:
                continue
            
            # mark current choice as explored in current DFS
            visited.add(pref)

            # Pref not chosen yet, assing to self
            if matching[pref] == -1:
                matching[pref] = node
                return True

            # Pref already chosen, try to see reassignment is possible
            previous = matching[pref]
            if dfs(previous, visited):
                matching[pref] = node
                return True
        return False


    matching = [-1] * num_spots
    for source in range(V):
        visited = set()
        if not dfs(source, visited):
            return False, []

    return True, matching
