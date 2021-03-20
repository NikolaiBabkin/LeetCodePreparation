from functools import lru_cache


class Solution:
    def longestCommonSubsequence_dp(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        n = len(text1)
        m = len(text2)
        curr = [0] * (m + 1)
        prev = [0] * (m + 1)
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if text1[i] == text2[j]:
                    curr[j] = 1 + prev[j + 1]
                else:
                    curr[j] = max(curr[j + 1], prev[j])

            prev = curr[:]

        return curr[0]


    def longestCommonSubsequence_recursive(self, text1: str, text2: str) -> int:
        @lru_cache(None)
        def longest(p1, p2):
            if p1 >= len(text1) or p2 >= len(text2):
                return 0

            if text1[p1] == text2[p2]:
                return 1 + longest(p1 + 1, p2 + 1)

            return max(longest(p1, p2 + 1), longest(p1 + 1, p2))

        return longest(0, 0)


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonSubsequence_dp("bsbininm", "jmjkbkjkv"))
