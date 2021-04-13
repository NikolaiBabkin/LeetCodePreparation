class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        queue = deque()
        res = []
        for i, num in enumerate(nums):
            while queue and queue[0] <= i - k:
                queue.popleft()

            while queue and nums[queue[-1]] < num:
                queue.pop()

            queue.append(i)
            res.append(nums[queue[0]])

        return res[k - 1:]

