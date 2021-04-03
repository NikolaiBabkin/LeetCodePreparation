class Solution:
    def canCross(self, stones: List[int]) -> bool:
        @lru_cache(None)
        def dp(n, k):
            res = 0
            if n == 0:
                if k != 1:
                    return 0
                return 1
            if stones[n] - k in stones_map:
                res = max(res, dp(stones_map[stones[n] - k], k))
            if stones[n] - (k + 1) in stones_map:
                res = max(res, dp(stones_map[stones[n] - (k + 1)], k+1))
            if k > 1 and stones[n] - (k - 1) in stones_map:
                res = max(res, dp(stones_map[stones[n] - (k - 1)], k-1))
            return res



        res = 0
        stones_map = dict()
        for i in range(len(stones)):
            stones_map[stones[i]] = i

        if len(stones_map) != len(stones):
            return False

        for stone in stones[:-1]:
            res = max(res, dp(len(stones) - 1, stones[-1] - stone))

        return res == 1

