class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        chars = dict()
        for ch in s:
            if ch in chars:
                chars[ch] += 1
            else:
                chars[ch] = 1
        cnt_odd = 0
        for ch, cnt in chars.items():
            if cnt % 2:
                cnt_odd += 1

        if cnt_odd == 0 or cnt_odd == 1:
            return True
        return False
