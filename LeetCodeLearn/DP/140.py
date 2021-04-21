class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        @lru_cache(None)
        def dp(start):
            if start >= len(s):
                return []

            res = []
            for end in range(start + 1, min(len(s), start + 10) + 1, 1):
                if s[start: end] not in words:
                    continue

                if end == len(s):
                    res.append(s[start: end])
                    continue

                if dp(end):
                    for sub_res in dp(end):
                        res.append(s[start: end] + ' ' + sub_res)

            return res


        words = set(wordDict)
        return list(set(dp(0)))

