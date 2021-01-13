class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        """
        Recursive solution
        Time Complexity: O(n*m)
        Space Complexity: O(1)
        """
        m = len(matrix)
        n = len(matrix[0])
        for start in range(-m+1, n):
            i = abs(min(0, start))
            j = max(0, start)
            start_elem = matrix[i][j]
            while i < m and j < n:
                if matrix[i][j] != start_elem:
                    return False
                i += 1
                j += 1
        return True

    def isToeplitzMatrix_cool(self, matrix: List[List[int]]) -> bool:
        """
        Recursive solution
        Time Complexity: O(n*m)
        Space Complexity: O(1)
        """
        return all(r == 0 or c == 0 or matrix[r-1][c-1] == val
                   for r, row in enumerate(matrix)
                   for c, val in enumerate(row))