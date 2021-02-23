class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Time Complexity: O(3^n * 4^m)
        Space Complexity: O(3^n * 4^m)
        """
        def backtracking(idx):
            if idx == len(digits):
                res.append(''.join(curr))
                return
            for letter in alphabet[int(digits[idx])]:
                curr.append(letter)
                backtracking(idx + 1)
                curr.pop()

        if len(digits) == 0:
            return []
        alphabet = {2: 'abc',
                    3: 'def',
                    4: 'ghi',
                    5: 'jkl',
                    6: 'mno',
                    7: 'pqrs',
                    8: 'tuv',
                    9: 'wxyz'}
        res = []
        curr = []
        backtracking(0)
        return res
