class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        Time Complexity: O(n^2)
        Space Complexity: O(n^2)
        """
        if numRows < 1:
            return []
        if numRows == 1:
            return [[1]]
        res = self.generate(numRows - 1)
        prev_level = res[-1]
        new_level = [1] * (len(prev_level) + 1)
        for i in range(1, len(prev_level)):
            new_level[i] = prev_level[i - 1] + prev_level[i]

        res.append(new_level)
        return res

