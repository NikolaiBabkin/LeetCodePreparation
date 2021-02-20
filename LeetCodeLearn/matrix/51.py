class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        Time Complexity: O(n!)
        Space Complexity: O(n)
        """
        def placing(row):
            for col in range(n):
                if is_under_attack(row, col):
                    continue

                new_placing = '.' * col + 'Q' + '.' * (n - col - 1)
                config.append(new_placing)
                update_under_attack(row, col)

                if len(config) == n:
                    res.append(config[:])
                else:
                    placing(row + 1)

                config.pop()
                update_under_attack(row, col, back=True)

        def is_under_attack(row, col):
            if under_attack[0][col]:
                return True
            if under_attack[1][row - col]:
                return True
            if under_attack[2][row + col]:
                return True
            return False

        def update_under_attack(row, col, back=False):
            new_val = 1 if back == False else 0
            under_attack[0][col] = new_val
            under_attack[1][row - col] = new_val
            under_attack[2][row + col] = new_val

        under_attack = [[0] * n, [0] * (2 * n - 1), [0] * (2 * n - 1)]
        res = []
        config = []
        placing(0)
        return res

