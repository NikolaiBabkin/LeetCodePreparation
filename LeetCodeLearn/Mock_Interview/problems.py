"""
Problems list

Easy: 169. Majority Element

Medium:

Hard:

"""


class ProblemSolution(object):
    def __init__(self):
        pass


class MajorityElement(ProblemSolution):
    """
    169. Majority Element
    https://leetcode.com/problems/majority-element/
    Given an array nums of size n, return the majority element.
    The majority element is the element that appears more than ⌊n / 2⌋ times.
    You may assume that the majority element always exists in the array.

    Example 1:
    Input: nums = [3,2,3]
    Output: 3

    Example 2:
    Input: nums = [2,2,1,1,1,2,2]
    Output: 2

    Constraints:
    n == nums.length
    1 <= n <= 5 * 104
    -231 <= nums[i] <= 231 - 1

    The task should be solved with TC = O(n) ans SC = O(1)
    Hints:
    1. Look at this problem as at voting results calculation
    2. What if we have just 2 candidates
    3. Can we calculate the result for 2 candidates using just one variable?
    4. What about 3 candidates

    Follow up:
    1. What if we don't now that the majority element always exists in the array?
    """
    def __init__(self):
        super().__init__()

    def majority_element_1(self, nums: list[int]) -> int:
        """
        Time Complexity: O(n*2)
        Space Complexity: O(1)
        """
        majority_min_count = len(nums) // 2
        for current in nums:
            count = sum(1 for num in nums if current == num)
            if count > majority_min_count:
                return current

    def majority_element_2(self, nums: list[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        counts = dict()
        majority_min_count = len(nums) // 2
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
            if counts[num] > majority_min_count:
                return num

    def majority_element_3(self, nums: list[int]) -> int:
        """
        Time Complexity: O(n*log(n))
        Space Complexity: O(1)
        """
        nums.sort()
        return nums[len(nums) // 2]

    def majority_element_4(self, nums: list[int]) -> int:
        """
        Boyer-Moore Voting Algorithm
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        current_elem = nums[0]
        count = 1
        for num in nums:
            if count == 0:
                current_elem = num
                count += 1
            else:
                if current_elem == num:
                    count += 1
                else:
                    count -= 1
        return current_elem
