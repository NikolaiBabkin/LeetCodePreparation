class Solution:
    def canCross_fast(self, stones: List[int]) -> bool:
        """
        Time Complexity: O(n^2)
        Space Complexity: O(n^2)
        """
        stones_map = dict()
        for stone in stones:
            stones_map[stone] = set()
        stones_map[stones[0]].add(0)
        for stone in stones:
            for k in stones_map[stone]:
                for i in range(-1, 2, 1):
                    if (k + i) > 0 and (stone + (k + i)) in stones_map:
                        stones_map[stone + (k + i)].add(k + i)

        return len(stones_map[stones[-1]]) > 0


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

