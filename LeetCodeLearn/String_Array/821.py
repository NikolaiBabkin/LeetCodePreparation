class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        c_indexes = [i for i, char in enumerate(s) if char == c]
        res = [0] * len(s)
        pointer_1 = 0
        pointer_2 = min(1, len(c_indexes) - 1)
        for i in range(len(res)):
            dist_1 = abs(c_indexes[pointer_1] - i)
            dist_2 = abs(c_indexes[pointer_2] - i)
            if dist_2 < dist_1:
                pointer_1 = pointer_2
                pointer_2 = min(pointer_2 + 1, len(c_indexes) - 1)
                res[i] = dist_2
            else:
                res[i] = dist_1
        return res
