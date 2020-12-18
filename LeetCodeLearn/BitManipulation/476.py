class Solution:
    def findComplement(self, num: int) -> int:
        """
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # n is a length of num in binary representation
        n = floor(log2(num)) + 1
        # bitmask has the same length as num and contains only ones 1...1
        bitmask = (1 << n) - 1
        # flip all bits
        return bitmask ^ num
