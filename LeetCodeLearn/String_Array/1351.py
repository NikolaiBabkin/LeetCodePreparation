class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        """
        Time Complexity: O(m + n)
        Space Complexity: O(1)
        """
        res = 0
        n = len(grid)
        m = len(grid[0])
        i = 0
        j = m-1
        while i < n:
            while j >= 0 and 0 > grid[i][j]:
                res += n - i
                j -= 1
            i += 1
        return res