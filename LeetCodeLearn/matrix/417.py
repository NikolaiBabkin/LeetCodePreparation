class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Time Complexity: O(n*m)
        Space Complexity: O(n*m)
        """
        def allowed_move(i, j, i_n, j_n, visited):
            res = True
            res &= 0 <= i_n < m
            res &= 0 <= j_n < n
            res &= (i_n, j_n) not in visited
            if res:
                res &= matrix[i][j] <= matrix[i_n][j_n]
            return res

        def bfs(visited, queue):
            while queue:
                i, j = queue.popleft()
                for move in moves:
                    i_n = i + move[0]
                    j_n = j + move[1]
                    if not allowed_move(i, j, i_n, j_n, visited):
                        continue
                    visited.add((i_n, j_n))
                    queue.append((i_n, j_n))

        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        if n == 0:
            return []
        moves = [(-1, 0), (0, -1), (0, 1), (1, 0)]

        a_reachable = set()
        for i in range(m):
            a_reachable.add((i, n - 1))
        for j in range(n):
            a_reachable.add((m - 1, j))
        a_queue = deque(a_reachable)

        p_reachable = set()
        for i in range(m):
            p_reachable.add((i, 0))
        for j in range(n):
            p_reachable.add((0, j))
        p_queue = deque(p_reachable)

        bfs(a_reachable, a_queue)
        bfs(p_reachable, p_queue)

        reachable = list(a_reachable.intersection(p_reachable))
        reachable = [list(itm) for itm in reachable]
        return reachable


