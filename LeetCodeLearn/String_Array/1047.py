class Solution:
    def removeDuplicates(self, s: str) -> str:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        stack = []
        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop(-1)
            else:
                stack.append(ch)
        return ''.join(stack)

