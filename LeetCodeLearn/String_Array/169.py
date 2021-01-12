class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        counter = 1
        elem = nums[0]
        for itm in nums[1:]:
            if counter == 0:
                elem = itm
                counter = 1
            else:
                if elem == itm:
                    counter += 1
                else:
                    counter -= 1
        return elem

