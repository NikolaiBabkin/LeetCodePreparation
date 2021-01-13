class Solution:
    def romanToInt(self, s: str) -> int:

        """
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        arabic = [1, 5, 10, 50, 100, 500, 1000]
        decoder = dict(zip(roman, arabic))
        res = 0
        pointer = 0
        while pointer < len(s):
            if pointer < (len(s) - 1) and decoder[s[pointer]] < decoder[s[pointer + 1]]:
                res += decoder[s[pointer + 1]] - decoder[s[pointer]]
                pointer += 2
            else:
                res += decoder[s[pointer]]
                pointer += 1
        return res
