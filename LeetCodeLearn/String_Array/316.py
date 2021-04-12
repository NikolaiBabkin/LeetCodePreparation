class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        seen = set()
        stack = []
        last_appear = {c: i for i, c in enumerate(s)}

        for i, c in enumerate(s):
            if c in seen:
                continue

            while stack and stack[-1] > c and i < last_appear[stack[-1]]:
                seen.discard(stack[-1])
                stack.pop()

            stack.append(c)
            seen.add(c)
        return ''.join(stack)

