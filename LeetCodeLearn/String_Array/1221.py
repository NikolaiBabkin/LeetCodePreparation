class Solution:
    @staticmethod
    def balancedStringSplit(self, s: str) -> int:

        """
        Time Complexity: O(len(res))
        Space Complexity: O(len(res))
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
    print(f'Test 1: {s.decompressRLElist([1,2,3,4]) == [2,4,4,4]}')