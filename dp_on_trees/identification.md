## How to identify?
Can easily identify tree -> node, root or something

how to identify its DP? ->

Consider longest path between two leaves: choose leaves such that the path between them is the longest

Solution: 

get the left height of the tree and right height of the tree at every node, then longest path at this node = LH + RH + 1

Traverse over every node and return the max value observed

problem asks for:

->traverse through each node in the tree: O(n)
->for each node do some O(|number of nodes in subtree|) operations

-> optimize recurseive calls by storing the solutions to the subproblems

So basically -> think of a recrusive solution to the problem and observe if there are any overlapping subproblems?
