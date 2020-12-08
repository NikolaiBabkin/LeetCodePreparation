class Solution:
    @staticmethod
    def balancedStringSplit(s: str) -> int:

        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        res = 0
        counter = 0
        for i in s:
            counter += 1 if i == 'R' else -1
            if counter == 0:
                res += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(f'Test 1: {s.balancedStringSplit("RLRRLLRLRL") == 4}')
    print(f'Test 1: {s.balancedStringSplit("RLLLLRRRLR") == 3}')
    print(f'Test 1: {s.balancedStringSplit("LLLLRRRR") == 1}')
    print(f'Test 1: {s.balancedStringSplit("RLRRRLLRLL") == 2}')