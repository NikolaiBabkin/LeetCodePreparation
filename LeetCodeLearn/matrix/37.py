class Solution:
    def solveSudoku(self, board) -> None:
        """
        Time Complexity: O((9!)**9)
        Space Complexity: O(9**2)
        """
        def backtrack(n):
            if n == 81:
                return True
            row = n // 9
            col = n % 9
            if board[row][col] != '.':
                if backtrack(n + 1):
                    return True
            else:
                candidates = get_candidates(row, col)
                for num in candidates:
                    add(num, row, col)
                    board[row][col] = str(num)
                    if backtrack(n + 1):
                        return True
                    delete(num, row, col)
                    board[row][col] = '.'

        def add(num, i, j):
            rows[i].add(num)
            cols[j].add(num)
            blocks[3* (i // 3) + j // 3].add(num)

        def delete(num, i, j):
            rows[i].remove(num)
            cols[j].remove(num)
            blocks[3* (i // 3) + j // 3].remove(num)

        def get_candidates(i, j):
            candidates = {i for i in range(1, 10)}
            candidates = candidates.difference(rows[i])
            candidates = candidates.difference(cols[j])
            candidates = candidates.difference(blocks[3* (i//3) + j//3])
            return candidates

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        blocks = [set() for _ in range(9)]
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    add(num, i, j)

        backtrack(0)


if __name__ == '__main__':
    s = Solution()
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    s.solveSudoku(board)
    print(board)