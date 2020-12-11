class Solution:
    def singleNumber_hashmap(self, nums):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        nums_dict = {}
        for i in nums:
            if i in nums_dict:
                nums_dict[i] += 1
            else:
                nums_dict[i] = 1

        for key, value in nums_dict.items():
            if value == 1:
                return key


    def singleNumber_bitwise(self, nums):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        res = 0
        for i in nums:
            res = res^i
        return res

if __name__ == '__main__':
    s = Solution()
    nums = [2,2,1]
    print(f'Test 1: {s.singleNumber_hashmap(nums) == 1}')
    nums = [4,1,2,1,2]
    print(f'Test 2: {s.singleNumber_hashmap(nums) == 4}')
    nums =[1]
    print(f'Test 3: {s.singleNumber_hashmap(nums) == 1}')


    nums = [2,2,1]
    print(f'Test 1: {s.singleNumber_bitwise(nums) == 1}')
    nums = [4,1,2,1,2]
    print(f'Test 2: {s.singleNumber_bitwise(nums) == 4}')
    nums =[1]
    print(f'Test 3: {s.singleNumber_bitwise(nums) == 1}')