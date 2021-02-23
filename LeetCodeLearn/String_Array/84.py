class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def find_largest(lo, hi):
            if lo == hi:
                return heights[lo]
            if lo > hi:
                return 0

            loc_min, idx_min = find_min(lo, hi)
            left = find_largest(lo, idx_min - 1)
            right = find_largest(idx_min + 1, hi)
            return max(left, right, loc_min * (hi - lo + 1))

        def find_min(lo, hi):
            loc_min, idx_min = heights[hi], hi
            for i in range(lo, hi):
                if heights[i] < loc_min:
                    loc_min, idx_min = heights[i], i

            return loc_min, idx_min

        return find_largest(0, len(heights) - 1)


if __name__ == '__main__':
    s = Solution()