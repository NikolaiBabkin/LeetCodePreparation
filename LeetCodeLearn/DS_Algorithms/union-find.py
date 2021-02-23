"""
Quick Union Find Algorithm implementation with weighted and half path improvements
Time Complexity
Find: O(1)
Union: O(1)
Connected: O(1)
Constructor: O(n)
"""


class QuickUnionFind:
    def __init__(self, vertices):
        vertices = list(set(vertices))
        self.rename = dict(zip(vertices, range(len(vertices))))
        self.roots = list(range(len(vertices)))
        self.sizes = [1] * len(vertices)

    def _find(self, p):
        i = p
        while self.roots[i] != i:
            self.roots[i] = self.roots[self.roots[i]]
            i = self.roots[i]
        return i

    def union(self, p, q):
        p = self.rename[p]
        q = self.rename[q]
        root_p = self._find(p)
        root_q = self._find(q)
        if root_p == root_q:
            return
        if self.sizes[root_p] < self.sizes[root_q]:
            self.roots[root_p] = root_q
            self.sizes[root_q] += self.sizes[root_p]
        else:
            self.roots[root_q] = root_p
            self.sizes[root_p] += self.sizes[root_q]

    def connected(self, p, q):
        p = self.rename[p]
        q = self.rename[q]
        return self._find(p) == self._find(q)

    def n_components(self):
        components = set()
        for i in self.roots:
            components.add(self._find(i))
        return len(components)


def test(grid):
    def add_connections(i, j):
        p = i * len(grid[0]) + j
        if i != len(grid) - 1:
            if grid[i + 1][j] == '1':
                uf.union(p, (i + 1) * len(grid[0]) + j)
        if j != 0:
            if grid[i][j - 1] == '1':
                uf.union(p, i * len(grid[0]) + j - 1)
        if j != len(grid[0]) - 1:
            if grid[i][j + 1] == '1':
                uf.union(p, i * len(grid[0]) + j + 1)

    islands = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                islands.append(i * len(grid[0]) + j)

    uf = QuickUnionFind(islands)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                add_connections(i, j)

    return uf.n_components()


if __name__ == '__main__':
    grid = [["1","0","1","1","1"]
            ,["1","0","1","0","1"]
            ,["1","1","1","0","1"]]

    print(test(grid))