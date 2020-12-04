import random

class Solution:
    @staticmethod
    def shuffle_ineffective(nums, n):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        res = [0] * 2 * n
        for i in range(n):
            res[2 * i] = nums[i]
        for i in range(n):
            res[2 * i + 1] = nums[i + n]
        return res

    @staticmethod
    def shuffle_effective(nums, n):
        """
        Bitwise approach
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        shift_len = 10
        for i in range(n):
            nums[i] = (nums[i] << shift_len) + nums[i + n]

        for i in range(n - 1, 0, -1):
            nums[2 * i] = nums[i]

        mask = (1 << shift_len) - 1
        for i in range(n):
            nums[2 * i + 1] = nums[2 * i] & mask
            nums[2 * i] >>= shift_len

        return nums


if __name__ == '__main__':
    s = Solution()
    cnt = 1000
    print(f'Test 1: {s.shuffle_effective(list(range(cnt)), int(cnt / 2)) == s.shuffle_ineffective(list(range(cnt)), int(cnt / 2))}')
    # print(s.shuffle_effective([2,5,1,3,4,7], 3))