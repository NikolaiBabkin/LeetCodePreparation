class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(26)
        """
        if str1 == str2:
            return True

        adj_list = dict()
        for ch in str1:
            adj_list[ch] = set()

        for i in range(len(str1)):
            adj_list[str1[i]].add(str2[i])

        for v in adj_list:
            if len(adj_list[v]) > 1:
                return False

        return len(set(str2)) < 26


