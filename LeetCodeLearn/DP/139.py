from functools import lru_cache


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Time Complexity: O(n*20*20)
        Space Complexity: O(n*20)
        """
        @lru_cache(None)
        def dp(k):
            if k == 0:
                return True
            res = False
            for i in range(max(0, k-20), k):
                res |= dp(i) & (s[i:k] in wordDict)
            return res

        wordDict = set(wordDict)
        return dp(len(s))

