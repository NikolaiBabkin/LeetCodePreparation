class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        next_gt = dict()
        stack = []
        for elem in nums2:
            while stack and elem > stack[-1]:
                next_gt[stack.pop()] = elem
            stack.append(elem)

        res = [-1] * len(nums1)
        for i, elem in enumerate(nums1):
            if elem in next_gt:
                res[i] = next_gt[elem]
        return res