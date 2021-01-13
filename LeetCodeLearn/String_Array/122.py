class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        profit = 0
        in_position = 0
        buy_price = -1
        for day in range(len(prices)):
            if in_position:
                if day == len(prices) - 1:
                    profit += prices[day] - buy_price
                elif prices[day] > prices[day + 1]:
                    profit += prices[day] - buy_price
                    in_position = 0
            else:
                if day != len(prices) - 1:
                    if prices[day] < prices[day+1]:
                        in_position = 1
                        buy_price = prices[day]

        return profit

