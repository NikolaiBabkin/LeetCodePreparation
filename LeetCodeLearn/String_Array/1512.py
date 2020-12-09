class Solution:
    def numIdenticalPairs(self, nums):
        def combination(n, k):
            a = 1
            for i in range(k + 1, n + 1):
                a *= i

            b = 1
            for i in range(1, n - k + 1):
                b *= i

            return a / b

        nums_dict = {}
        for num in nums:
            if num in nums_dict.keys():
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1

        res = 0
        for key, value in nums_dict.items():
            if value > 1:
                res += combination(value, 2)

        return int(res)


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 1, 1, 3]
    print(f'Test 1: {s.numIdenticalPairs(nums)}')