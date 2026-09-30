# Two approaches to Dijkstras

## Standard Dijkstras with push time updates
```python
dist = [float('inf')] * n
dist[src] = 0
heap = [(0, src)]
visited = [False] * n

while heap:
    curr_dist, curr_node = heapq.heappop(heap)
    if visited[curr_node]: continue

    visited[curr_node] = True
    for nbr, wt in adj[curr_node]:
        new_dist = curr_dist + wt
        if new_dist < dist[nbr]:
            dist[nbr] = new_dist
            heapq.heappush(heap, (new_dist, nbr))
```
This is the standard dijkstras implementation when there is only one dimension we are tracking and trying to optimize for (ex. dist here)

We can also avoid having the visited array altogether because we can rely on the optimal value in dist array to avoid processing heap entries that are stale.

```python
dist = [float('inf')] * n
dist[src] = 0
heap = [(0, src)]

while heap:
    curr_dist, curr_node = heapq.heappop(heap)
    if dist[curr_node] < curr_dist: continue 
    # stale entry: a cheaper path to curr_node was pushed later,
    # and it pops before this one, so expanding this adds nothing

    for nbr, wt in adj[curr_node]:
        new_dist = curr_dist + wt
        if new_dist < dist[nbr]:
            dist[nbr] = new_dist
            heapq.heappush(heap, (new_dist, nbr))
```

## Pop-time update

Here, dist is written only when a node is popped, never when it's pushed. Because the heap pops in increasing order, the first pop of a node is its best value, so dist doubles as the visited array.

```python

while heap:
    curr_dist, curr_node = heapq.heappop(heap)
    if dist[curr_node] <= curr_dist: continue

    dist[curr_node] = curr_dist
    for nbr, wt in adj[curr_node]:
        new_dist = curr_dist + wt
        if new_dist < dist[nbr]: 
              # This check is optional and purely an optimization step.
              # The algorithm also works without it because stale values are
              # gated at pop time.
            heapq.heappush(heap, (new_dist, nbr))
```

Interesting things happen on a multi-dimension Dijkstras though. Say we have two
dimensions, dimA and dimB, and want the best dimA within some constraint on
dimB. Ex. the cheapest cost (dimA) within k stops (dimB).

Order the heap by one dimension (cost) and keep an array for the other
(best stops per node), written only at pop time.

Intuition: suppose node X was earlier popped with (costX1, stopsX1), and
stopsX1 was recorded then. Now we pop (costX2, stopsX2). The heap pops in
increasing cost, so costX2 >= costX1. The new state can only be useful if it
has strictly fewer stops (stopsX2 < stopsX1). Otherwise it's no better in
either dimension than a real path we've already expanded, so it's safe to
skip.

This is why the write must happen at pop time: the pop order is what
guarantees costX1 <= costX2. A value written at push time may come from a
state still in the heap, so that guarantee is gone.

```python
stops = [float('inf')] * n
heap = [(0, 0, src)] # cost, stops, node

while heap:
    curr_cost, curr_stops, curr_node = heapq.heappop(heap)
    if curr_node == dst: return curr_cost
    if stops[curr_node] <= curr_stops: continue

    stops[curr_node] = curr_stops
    for nbr, wt in adj[curr_node]:
        new_stops = curr_stops + 1
        if new_stops < stops[nbr] and new_stops <= max_stops:
            heapq.heappush(heap, (curr_cost + wt, new_stops, nbr))
    
return -1 # no valid path
```

Since the heap ordering gurantees popping in increasing order of costs, the first time a destination node is popped is the optimal cost for it, hence we can also return early!

We can also do it the other way round by keeping stops as our dimA and cost as our dimB for the heap ordering:

```python
cost = [float('inf')] * n
heap = [(0, 0, src)] # stops, cost, node

while heap:
    curr_stops, curr_cost, curr_node = heapq.heappop(heap)
    if cost[curr_node] <= curr_cost: continue

    cost[curr_node] = curr_cost
    for nbr, wt in adj[curr_node]:
        new_cost = curr_cost + wt
        if new_cost < cost[nbr] and curr_stops + 1 <= max_stops:
            heapq.heappush(heap, (curr_stops + 1, new_cost, nbr))
    
return cost[dst] if cost[dst] != float('inf') else -1
```

Note here that while this works, we do not have the guarantee that the first time we pop destination node will be the optimal cost state because the heap ordering gurantees popping in increasing order of stops this time