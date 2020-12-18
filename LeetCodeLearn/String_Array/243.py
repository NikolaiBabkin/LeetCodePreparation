class Solution:
    def shortestDistance(self, words, word1, word2):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        it1 = it2 = None
        res = len(words)
        for i, word in enumerate(words):
            if word == word1:
                it1 = i
                if it2 is not None:
                    res = min(res, it1 - it2)
            if word == word2:
                it2 = i
                if it1 is not None:
                    res = min(res, it2 - it1)
        return res