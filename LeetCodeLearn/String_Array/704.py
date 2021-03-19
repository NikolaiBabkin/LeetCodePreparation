class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Time Complexity: O(log(n))
        Space Complexity: O(1)
        """
        if not nums:
            return -1

        l, r = 0, len(nums)
        while l + 1 < r:
            mid = l + (r - l) // 2
            if target < nums[mid]:
                r = mid
            else:
                l = mid

        return l if nums[l] == target else -1


