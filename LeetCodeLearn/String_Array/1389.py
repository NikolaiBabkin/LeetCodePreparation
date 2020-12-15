class Solution:
    def createTargetArray(self, nums, index):
        """
        Brute force
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        res = []
        for i in range(len(index)):
            if index[i] == len(res):
                res.append(nums[i])
            else:
                res = res[:index[i]] + [nums[i]] + res[index[i]:]
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [0, 1, 2, 3, 4]
    index = [0, 1, 2, 2, 1]
    output = [0,4,1,3,2]
    print(f'Test 1: {s.createTargetArray(nums, index) == output}')

    nums = [0, 1, 2, 3, 4]
    index = [0, 1, 2, 2, 1]
    output = [0,4,1,3,2]
    print(f'Test 1: {s.createTargetArray(nums, index) == output}')

    nums = [1,2,3,4,0]
    index = [0,1,2,3,0]
    output = [0,1,2,3,4]
    print(f'Test 1: {s.createTargetArray(nums, index) == output}')