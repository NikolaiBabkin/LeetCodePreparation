class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        """
        Time Complexity: O(n*log(n))
        Space Complexity: O(n)
        """
        def neighbours(i, j):
            for di, dj in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                if (i + di, j + dj) in visited:
                    continue
                if not (0 <= i + di < m):
                    continue
                if not (0 <= j + dj < n):
                    continue
                yield (i + di, j + dj)

        res = 0
        curr_max = 0
        heap = set()
        visited = set()
        m, n = len(heightMap), len(heightMap[0])
        for i in range(m):
            heap.add((heightMap[i][0], i, 0))
            visited.add((i, 0))
            heap.add((heightMap[i][n - 1], i, n - 1))
            visited.add((i, n - 1))

        for j in range(n):
            heap.add((heightMap[0][j], 0, j))
            visited.add((0, j))
            heap.add((heightMap[m - 1][j], m - 1, j))
            visited.add((m - 1, j))

        heap = list(heap)
        heapq.heapify(heap)
        while heap:
            val, i, j = heapq.heappop(heap)
            curr_max = max(curr_max, val)
            for i_n, j_n in neighbours(i, j):
                val_n = heightMap[i_n][j_n]
                if val_n < curr_max:
                    res += curr_max - val_n
                heapq.heappush(heap, (val_n, i_n, j_n))
                visited.add((i_n, j_n))

        return res


