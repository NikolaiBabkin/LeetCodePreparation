class Solution:
    def minTimeToVisitAllPoints(self, points) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if len(points) == 1:
            return 0
        res = 0
        prev = points[0]
        for curr in points[1:]:
            res += max(abs(curr[0] - prev[0]), abs(curr[1] - prev[1]))
            prev = curr
        return res


if __name__ == '__main__':
    s = Solution()
    points = [[3,2],[-2,2]]
    print(f'Test 1: {s.minTimeToVisitAllPoints(points) == 5}')