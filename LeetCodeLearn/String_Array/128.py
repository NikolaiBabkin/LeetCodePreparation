class Solution1:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    def longestConsecutive(self, nums):
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak


class UnionFind:
    def __init__(self, arr):
        self.decoder = dict(zip(arr, range(len(arr))))
        self.parents = list(range(len(arr)))
        self.sizes = [1] * len(arr)

    def _find(self, p):
        while p != self.parents[p]:
            self.parents[p] = self.parents[self.parents[p]]
            p = self.parents[p]
        return p

    def union(self, p, q):
        p = self.decoder[p]
        if q not in self.decoder:
            return
        q = self.decoder[q]
        root_p = self._find(p)
        root_q = self._find(q)
        if root_p == root_q:
            return
        if self.sizes[root_p] < self.sizes[root_q]:
            self.parents[root_p] = root_q
            self.sizes[root_q] += self.sizes[root_p]
        else:
            self.parents[root_q] = root_p
            self.sizes[root_p] += self.sizes[root_q]

    def biggest_component(self):
        res = 0
        for idx, node in enumerate(self.parents):
            if idx == node:
                res = max(res, self.sizes[node])
        return res


class Solution2:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    def longestConsecutive(self, nums):
        uf = UnionFind(nums)
        for num in nums:
            uf.union(num, num - 1)
            uf.union(num, num + 1)
        return uf.biggest_component()
