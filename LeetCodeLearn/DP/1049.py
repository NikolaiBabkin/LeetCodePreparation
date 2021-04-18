class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        @lru_cache(None)
        def dp(c, i):
            if c <= 0:
                return 0
            if i >= len(stones):
                return 0
            p1 = 0
            if c >= stones[i]:
                p1 = dp(c - stones[i], i + 1) + stones[i]
            p2 = dp(c, i + 1)

            return max(p1, p2)

        total_vol = sum(stones)
        capacity = total_vol // 2
        return total_vol - 2 * dp(capacity, 0)

