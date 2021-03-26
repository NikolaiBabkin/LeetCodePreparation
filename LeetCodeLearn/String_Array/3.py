class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        p1 = 0
        visited = set()
        max_len = 0
        for p2 in range(len(s)):
            while s[p2] in visited:
                visited.remove(s[p1])
                p1 += 1

            visited.add(s[p2])
            max_len = max(max_len, len(visited))

        return max_len