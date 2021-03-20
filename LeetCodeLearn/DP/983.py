class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        @lru_cache(None)
        def cost_calc(k):
            if k >= len(days):
                return 0

            p = cost_calc(k + 1) + costs[0]
            l = 0
            while k + l < len(days) and days[k + l] - days[k] < 7:
                l += 1
            p = min(p, cost_calc(k + l) + costs[1])

            l = 0
            while k + l < len(days) and days[k + l] - days[k] < 30:
                l += 1

            p = min(p, cost_calc(k + l) + costs[2])

            return p

        return cost_calc(0)


