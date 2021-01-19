class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        ch_counter = {c: i for i, c in enumerate(s)}

        res = []
        max_app = 0
        last_split = -1
        for i in range(len(s)):
            max_app = max(max_app, ch_counter[s[i]])
            if max_app == i:
                size = i - last_split
                last_split = i
                res.append(size)

        return res
