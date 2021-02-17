class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Time Complexity: O(n + m)
        Space Complexity: O(1)
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        height = len(matrix) - 1
        width = 0
        while width != len(matrix[0]) and height != -1:
            if matrix[height][width] == target:
                return True

            if matrix[height][width] < target:
                width += 1
            else:
                height -= 1
                continue

        return False