class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        stack = [(s[0], 1)]
        for ch in s[1:]:
            if stack and ch == stack[-1][0]:
                new_counter = stack[-1][1] + 1
                stack.append((ch, new_counter))

                if new_counter == k:
                    for _ in range(k):
                        stack.pop(-1)
            else:
                stack.append((ch, 1))

        return ''.join([itm[0] for itm in stack])