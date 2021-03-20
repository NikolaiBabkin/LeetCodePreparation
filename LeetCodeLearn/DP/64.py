class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        Time Complexity: O(n*m)
        Space Complexity: O(n)
        """
        m = len(grid)
        n = len(grid[0])
        prev = [math.inf] * (n + 1)
        curr = [0] * (n + 1)
        for i in range(m):
            for j in range(n):
                curr[j + 1] = grid[i][j] + min(curr[j], prev[j + 1])

            prev = curr[:]
            curr[0] = math.inf

        return curr[-1]

