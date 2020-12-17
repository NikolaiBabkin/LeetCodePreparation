class Solution:
    def maximum69Number(self, num: int) -> int:
        res = [' '] * len(str(num))
        changes = 1
        for i, digit in enumerate(str(num)):
            if changes:
                if digit == '6':
                    digit = '9'
                    changes -= 1
            res[i] = digit
        return int(''.join(res))