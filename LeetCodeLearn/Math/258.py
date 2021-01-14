class Solution:
    def addDigits(self, num: int) -> int:
        """
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if num:
            return 9 if num % 9 == 0 else num % 9
        return 0