from DS_Algorithms.sorting.my_sort import MySort


class Solution:
    def arrayPairSum_hashmap(self, nums):
        """
        Time Complexity: O(n)
        Space Complexity: O(20000)
        """
        def hash_sort(arr):
            hashmap = [0] * 20001
            for i in arr:
                hashmap[i + 10000] += 1
            it = 0
            for i in range(len(hashmap)):
                if hashmap[i]:
                    arr[it:(it + hashmap[i])] = [i - 10000] * hashmap[i]
                    it += hashmap[i]

        hash_sort(nums)
        res = 0
        for i in range(0, len(nums), 2):
            res += nums[i]
        return res

    def arrayPairSum(self, nums):
        """
        Time Complexity: O(n log(n))
        Space Complexity: O(n)
        """
        def merge_sort(arr):
            def _merge(left, mid, right):
                helper = [0] * (right - left)
                it1 = it2 = 0
                while (left + it1 < mid) and (mid + it2 < right):
                    if arr[left + it1] <= arr[mid + it2]:
                        helper[it1 + it2] = arr[left + it1]
                        it1 += 1
                    else:
                        helper[it1 + it2] = arr[mid + it2]
                        it2 += 1

                while left + it1 < mid:
                    helper[it1 + it2] = arr[left + it1]
                    it1 += 1

                while mid + it2 < right:
                    helper[it1 + it2] = arr[mid + it2]
                    it2 += 1

                arr[left: right] = helper

            def _merge_sort(left, right):
                if left + 1 < right:
                    mid = int((right + left) / 2)
                    _merge_sort(left, mid)
                    _merge_sort(mid, right)
                    _merge(left, mid, right)

            _merge_sort(0, len(arr))

        merge_sort(nums)
        res = 0
        for i in range(0, len(nums), 2):
            res += nums[i]
        return res



# def hash_sort(arr):
#     hashmap = [0] * 21
#     for i in arr:
#         hashmap[i + 10] += 1
#     it = 0
#     for i in (hashmap):
#         if hashmap[i]:
#             arr[it:(it + hashmap[i])] = i - 10
#             it += hashmap[i]
#     return arr


if __name__ == '__main__':
    s = Solution()
    nums = [1, 4, 3, 2]
    print
    print(f'Test1: {s.arrayPairSum_hashmap(nums) == 4}')

    nums = [6,2,6,5,1,2]
    print(f'Test1: {s.arrayPairSum_hashmap(nums) == 9}')