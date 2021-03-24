class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        stack = []
        for i in num:
            while stack and k and stack[-1] > i:
                stack.pop()
                k -= 1
            stack.append(i)
        stack = stack[:-k] if k else stack
        return "".join(stack).lstrip('0') or "0"

