class Solution:
    def calPoints(self, ops: List[str]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        scores = []
        for op in ops:
            if op == 'D':
                scores.append(scores[-1] * 2)
            elif op == 'C':
                scores.pop(-1)
            elif op == '+':
                scores.append(sum(scores[-2:]))
            else:
                scores.append(int(op))
        return sum(scores)
