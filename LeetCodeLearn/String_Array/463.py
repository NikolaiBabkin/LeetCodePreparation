class Solution:
    def islandPerimeter(self, grid) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        res = 0
        for i in range(len(grid)):
            up = i - 1
            down = i + 1
            for j in range(len(grid[0])):
                left = j - 1
                right = j + 1
                if grid[i][j]:
                    if (up < 0):
                        res += 1
                    elif grid[up][j] == 0:
                        res += 1

                    if down >= len(grid):
                        res += 1
                    elif grid[down][j] == 0:
                        res += 1

                    if left < 0:
                        res += 1
                    elif grid[i][left] == 0:
                        res += 1

                    if right >= len(grid[0]):
                        res += 1
                    elif grid[i][right] == 0:
                        res += 1
        return res


if __name__ == '__main__':
    s = Solution()
    grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    print(s.islandPerimeter(grid))