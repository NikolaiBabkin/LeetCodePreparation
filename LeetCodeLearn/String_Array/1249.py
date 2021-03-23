class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        s = [ch for ch in s]
        stack = []
        for idx, ch in enumerate(s):
            if ch in ['(', ')']:
                if stack and stack[-1][0] + ch == '()':
                    stack.pop()
                else:
                    stack.append((ch, idx))

        to_drop = {idx for ch, idx in stack}
        res = []
        for idx, ch in enumerate(s):
            if idx in to_drop:
                continue
            res.append(ch)

        return ''.join(res)

