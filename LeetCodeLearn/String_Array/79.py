class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def find(i_s, j_s, p):
            if p == len(word) - 1:
                return True
            for di, dj in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
                i_n, j_n = i_s + di, j_s + dj
                if (i_n, j_n) in visited:
                    continue
                if i_n < 0 or i_n >=m or j_n < 0 or j_n >=n:
                    continue
                if board[i_n][j_n] != word[p+1]:
                    continue

                visited.add((i_n, j_n))
                if find(i_n, j_n, p+1):
                    return True
                visited.discard((i_n, j_n))

            return False


        m = len(board)
        n = len(board[0])
        start = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    start.append([i, j])

        if len(start) == 0:
            return False

        for i_s, j_s in start:
            visited = set([(i_s, j_s)])
            if find(i_s, j_s, 0):
                return True

        return False


