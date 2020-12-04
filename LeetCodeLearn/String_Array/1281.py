class Solution:
    def subtractProductAndSum(self, n: int) -> int:"""
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        dig_sum, dig_prod = 0, 1
        while n:
            digit = n % 10
            dig_sum += digit
            dig_prod *= digit
            n //= 10
        return dig_prod - dig_sum

if __name__ == '__main__':
    s = Solution()
    print(s.subtractProductAndSum(1234))