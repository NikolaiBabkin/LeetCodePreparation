class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        prev = cost[0]
        curr = cost[1]
        for i in range(2, len(cost)):
            next = min(prev, curr) + cost[i]
            prev = curr
            curr = next

        return min(prev, curr)

