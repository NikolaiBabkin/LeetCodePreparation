class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        prev = nums[0]
        curr = max(prev, nums[1])
        for i in range(2, len(nums)):
            next = max(prev + nums[i], curr)
            prev = curr
            curr = next

        return curr
