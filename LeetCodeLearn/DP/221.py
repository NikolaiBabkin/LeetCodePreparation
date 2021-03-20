class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        Time Complexity: O(m*n)
        Space Complexity: O(n)
        """
        m = len(matrix)
        n = len(matrix[0])
        prev = [0] * (n + 1)
        curr = [0] * (n + 1)
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "0":
                    curr[j + 1] = 0
                else:
                    val = 0
                    val = min(curr[j], prev[j], prev[j + 1])
                    val += 1
                    res = max(res, val)
                    curr[j + 1] = val
            prev = curr[:]

        return res ** 2

