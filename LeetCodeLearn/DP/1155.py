class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        """
        Time Complexity: O(target*d)
        Space Complexity: O(target*d)
        """
        @lru_cache(None)
        def ways(sub_target, dice_remain):
            if sub_target == 0 and dice_remain == 0:
                return 1
            if sub_target <= 0 or dice_remain <= 0:
                return 0

            res = 0
            for i in range(1, f + 1):
                res += ways(sub_target - i, dice_remain - 1)
                res %= 10 ** 9 + 7

            return res

        return ways(target, d)

