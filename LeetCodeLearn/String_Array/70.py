import functools


class Solution:
    @functools.lru_cache(maxsize=None)
    def climbStairs(self, n: int) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if n <= 2:
            return n
        return self.climbStairs(n - 2) + self.climbStairs(n - 1)

    def climbStairs_2(self, n: int) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if n <= 2:
            return n

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(38))
