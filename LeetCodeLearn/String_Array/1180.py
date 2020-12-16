class Solution:
    def countLetters(self, S: str) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        res = 0
        if len(S) == 1:
            return 1
        it1 = 0
        for it2 in range(1, len(S)):
            if S[it2] != S[it2 - 1]:
                substr_len = it2 - it1
                res += int((substr_len + 1) * (substr_len / 2))
                it1 = it2
            if it2 == len(S) - 1:
                substr_len = it2 - it1 + 1
                res += int((substr_len + 1) * (substr_len / 2))
        return res


if __name__ == '__main__':
    s = Solution()
    S = "aaaba"
    print(s.countLetters(S))