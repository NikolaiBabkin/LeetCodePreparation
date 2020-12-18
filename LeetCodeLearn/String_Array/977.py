class Solution:
    def sortedSquares(self, nums):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        res = [0] * len(nums)
        mid_point = 0
        for i in range(len(nums)):
            mid_point = i
            if nums[i] >= 0:
                break
            nums[i] = abs(nums[i])

        it1 = mid_point - 1
        it2 = mid_point
        it_res = 0
        while it1 >= 0 and it2 < len(nums):
            if nums[it1] <= nums[it2]:
                res[it_res] = nums[it1]**2
                it1 -= 1
            else:
                res[it_res] = nums[it2]**2
                it2 += 1
            it_res += 1
        while it1 >= 0:
            res[it_res] = nums[it1]**2
            it1 -= 1
            it_res += 1
        while it2 < len(nums):
            res[it_res] = nums[it2]**2
            it2 += 1
            it_res += 1

        return res
