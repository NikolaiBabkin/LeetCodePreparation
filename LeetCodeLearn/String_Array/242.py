class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if len(s) != len(t):
            return False
        s_cnt_map = dict()
        for ch in s:
            if ch in s_cnt_map:
                s_cnt_map[ch] += 1
            else:
                s_cnt_map[ch] = 1

        for ch in t:
            if ch in s_cnt_map:
                s_cnt_map[ch] -= 1
            else:
                return False

        for ch in s_cnt_map:
            if s_cnt_map[ch] != 0:
                return False

        return True

