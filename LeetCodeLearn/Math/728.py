class Solution:
    def selfDividingNumbers(self, left, right):
        """
        Time Complexity: O((left - right) * log(right))
        Space Complexity: O(left - right)
        """
        res = []
        for num in range(left, right + 1):
            is_self_div = 1
            for i in str(num):
                if int(i) == 0:
                    is_self_div = 0
                    break
                if num % int(i):
                    is_self_div = 0
                    break
            if is_self_div:
                res.append(num)
        return res


if __name__ == '__main__':
    s = Solution()
    print(f'Test 1: {s.selfDividingNumbers(1, 202) }')