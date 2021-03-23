class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        def allowed_move(i, j):
            res = True
            res &= 0 <= i < m
            res &= 0 <= j < n
            res &= (i, j) not in visited
            if res:
                res &= rooms[i][j] != -1
            return res

        queue = deque()
        m = len(rooms)
        n = len(rooms[0])
        visited = set()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j, 0))
                    visited.add((i, j))

        moves = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        while queue:
            i, j, dist = queue.popleft()
            rooms[i][j] = dist
            for move in moves:
                i_n = i + move[0]
                j_n = j + move[1]
                if not allowed_move(i_n, j_n):
                    continue
                visited.add((i_n, j_n))
                queue.append((i_n, j_n, dist + 1))