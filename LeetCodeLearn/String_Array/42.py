class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not height:
            return 0

        left_max = [-1] * len(height)
        curr_max = -1
        for idx, h in enumerate(height):
            curr_max = max(curr_max, h)
            left_max[idx] = curr_max

        right_max = [-1] * len(height)
        curr_max = -1
        for idx, h in enumerate(height[::-1]):
            curr_max = max(curr_max, h)
            right_max[idx] = curr_max

        right_max = right_max[::-1]

        water = [-1] * len(height)
        for i in range(len(height)):
            water[i] = min(right_max[i], left_max[i]) - height[i]

        return sum(water)
