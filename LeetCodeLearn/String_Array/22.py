class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Time Complexity: O(Catalan(n))
        Space Complexity: O(n)
        """
        def backtracking(op, cl):
            if op == n:
                sub_res = ''.join(curr)
                sub_res += ')' * (n - cl)
                res.append(sub_res)
                return
            curr.append('(')
            op += 1
            backtracking(op, cl)
            curr.pop()
            op -= 1

            if op > cl:
                curr.append(')')
                cl += 1
                backtracking(op, cl)
                curr.pop()
                cl -= 1

        res = []
        curr = []
        op = 0
        cl = 0
        backtracking(op, cl)
        return res
