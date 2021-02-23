class Solution:
    def permute(self, arr: List[int]) -> List[List[int]]:
        """
        Time Complexity: O(n!)
        Space Complexity: O(n!)
        """
        def backtracking():
            if len(curr) == len(arr):
                res.append(curr[:])
                return
            visited = set(curr)
            for num in arr:
                if num not in visited:
                    curr.append(num)
                    backtracking()
                    curr.pop()

        if len(arr) == 0:
            return arr
        res = []
        curr = []
        backtracking()
        return res