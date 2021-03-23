class Solution:
    def __init__(self, w: List[int]):
        """
        Time Complexity: O(n*log(n))
        Space Complexity: O(n)
        """
        sum_w = sum(w)
        for i in range(len(w)):
            w[i] = w[i] / sum_w

        for i in range(1, len(w)):
            w[i] += w[i - 1]

        self.w = w

    def pickIndex(self) -> int:
        rand = random.random()

        l = 0
        r = len(self.w)
        while l + 1 < r:
            m = l + (r - l) // 2
            if rand < self.w[m]:
                r = m
            else:
                l = m

        return l if rand < self.w[l] else r

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()