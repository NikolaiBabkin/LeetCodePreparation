class Solution:
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums

if __name__ == '__main__':
    s = Solution()
    print(f'Test 1: {s.runningSum([1,2,3,4]) == [1,3,6,10]}')
    print(f'Test 2: {s.runningSum([1,1,1,1,1]) == [1,2,3,4,5]}')
    print(f'Test 3: {s.runningSum([3,1,2,10,1]) == [3,4,6,16,17]}')