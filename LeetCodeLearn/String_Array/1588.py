class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        res, n = 0, len(arr)
        for i, a in enumerate(arr):
            total = (i + 1) * (n - i)
            odd = total // 2
            if total % 2 == 1:
                odd += 1
            res += odd * a
        return res
