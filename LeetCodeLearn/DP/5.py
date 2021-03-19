class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        if len(s) < 2:
            return s

        res = (0, 0)
        for i in range(len(s)):
            for start, end in [(i, i), (i, i+1)]:
                while start >= 0 and end < len(s):
                    if s[start] != s[end]:
                            break

                    if end - start > res[1] - res[0]:
                        res = (start, end)

                    start -= 1
                    end += 1

        return s[res[0]:(res[1]+1)]