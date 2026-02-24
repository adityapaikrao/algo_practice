class UnionFind:
    def __init__(self, n: int) -> None:
        self.size = [1] * n
        self.root = [i for i in range(n)]
    
    def find(self, x: int) -> int:
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x: int, y: int) -> None:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return  # already in the same component

        if self.size[root_x] >= self.size[root_y]:
            self.root[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        else:
            self.root[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        
        return

