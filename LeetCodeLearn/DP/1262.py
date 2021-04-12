class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        dp = [0, 0, 0]
        for num in nums:
            for i in dp[:]:
                dp[(i + num) % 3] = max(i + num, dp[(i + num) % 3])
        return dp[0]

#         def update_reminder(arr, num):
#             heapq.heappush(arr, - num)
#             if len(arr) > 2:
#                 heapq.heappop(arr)

#         total_sum = 0
#         reminder_1 = []
#         reminder_2 = []
#         for num in nums:
#             total_sum += num
#             if num % 3 == 1:
#                 update_reminder(reminder_1, num)
#             if num % 3 == 2:
#                 update_reminder(reminder_2, num)

#         if total_sum % 3 == 1:
#             if len(reminder_2) == 2:
#                 total_sum -= min(-max(reminder_1), -sum(reminder_2))
#             else:
#                 total_sum -= -max(reminder_1)
#         if total_sum % 3 == 2:
#             if len(reminder_1) == 2:
#                 total_sum -= min(-max(reminder_2), -sum(reminder_1))
#             else:
#                 total_sum -= -max(reminder_2)

#         return total_sum

