class Solution:
    @staticmethod
    def decompressRLElist(nums):
        """
        Time Complexity: O(len(res))
        Space Complexity: O(len(res))
        """
        res_len = 0
        for i in range(0, len(nums), 2):
            res_len += nums[i]

        res = [0] * res_len
        start = 0
        for i in range(0, len(nums), 2):
            curr_len = nums[i]
            res[start : (start + curr_len)] = [nums[i + 1]] * curr_len
            start += curr_len

        return res


    @staticmethod
    def decompressRLElist_2(nums):

        """
        Time Complexity: O(len(res))
        Space Complexity: O(len(res))
        """
        return [x for a, b in zip(nums[0::2], nums[1::2]) for x in [b] * a]


if __name__ == '__main__':
    s = Solution()
    print(f'Test 1: {s.decompressRLElist([1,2,3,4]) == [2,4,4,4]}')
    print(f'Test 1: {s.decompressRLElist([1,1,2,3]) == [1,3,3]}')

    print(f'Test 1: {s.decompressRLElist_2([1,2,3,4]) == [2,4,4,4]}')
    print(f'Test 1: {s.decompressRLElist_2([1,1,2,3]) == [1,3,3]}')