class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[slow] == 0 and nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            if nums[slow] != 0:
                slow += 1

        return nums

