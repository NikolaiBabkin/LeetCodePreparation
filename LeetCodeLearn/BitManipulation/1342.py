class Solution:
    @staticmethod
    def numberOfSteps(num: int) -> int:
        """
        Time Complexity: O(log(n))
        Space Complexity: O(1)
        """
        counter = 0
        while num:
            if num % 2:
                num -= 1
            else:
                num /= 2
            counter += 1
        return counter


    @staticmethod
    def numberOfSteps_bit(num: int) -> int:
        """
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        q_1 = 0
        q_0 = 0
        while num:
            if num&1:
                q_1 += 1
            else:
                q_0 += 1
            num = num >> 1
        return max(0, 2 * q_1 + q_0 - 1)

if __name__ == '__main__':
    s = Solution()
    print(f'Test 1: {s.numberOfSteps(14) == 6}')
    print(f'Test 1: {s.numberOfSteps(8) == 4}')
    print(f'Test 1: {s.numberOfSteps(123) == 12}')


    print(f'Test 1: {s.numberOfSteps_bit(1)}')
    print(f'Test 1: {s.numberOfSteps_bit(8)}')
    print(f'Test 1: {s.numberOfSteps_bit(123)}')