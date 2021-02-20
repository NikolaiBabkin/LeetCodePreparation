class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def combinations(start):
            if len(curr) == k:
                res.append(curr[:])
                return
            for num in range(start, n + 1):
                curr.append(num)
                combinations(num + 1)
                curr.pop()

        res = []
        curr = []
        combinations(1)
        return res


