class Solution:
    def judgeCircle(self, moves: str) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        vert = horis = 0
        for s in moves:
            if s == 'R':
                horis += 1
            elif s == 'L':
                horis -= 1
            elif s == 'U':
                vert += 1
            else:
                vert -= 1

        if vert == horis == 0:
            return True

        return False


if __name__ == '__main__':
    s = Solution()
    items = "UD"
    output = True
    print(f'Test 1: {s.judgeCircle(items) == output}')