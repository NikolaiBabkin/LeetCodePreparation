class Solution:
    def smallerNumbersThanCurrent_fast_and_cool(nums):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        count = [0] * 102
        for num in nums:
            count[num + 1] += 1
        for i in range(1, 102):
            count[i] += count[i - 1]
        return [count[num] for num in nums]

    @staticmethod
    def smallerNumbersThanCurrent_fast(nums):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        result = [0] * len(nums)
        positions = {}
        for i, num in enumerate(nums):
            if num in positions.keys():
                positions[num].append(i)
            else:
                positions[num] = [i]

        nums = set(nums)
        nums = [i for i in range(101) if i in nums]
        counter = 0
        for num in nums:
            for pos in positions[num]:
                result[pos] = counter
            counter += len(positions[num])

        return result

    @staticmethod
    def smallerNumbersThanCurrent(nums):
        """
        Time Complexity: O(nlog(n))
        Space Complexity: O(n)
        """
        def merge_sort(arr):
            def _merge_sort(left, right):
                if left + 1 < right:
                    mid = int((left + right) / 2)
                    _merge_sort(left, mid)
                    _merge_sort(mid, right)
                    merge(left, mid, right)

            def merge(left, mid, right):
                helper = [0] * (right - left)
                it1 = it2 = 0
                while (left + it1 < mid) & (mid + it2 < right):
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

                arr[left:right] = helper

            _merge_sort(0, len(arr))

        result = [0] * len(nums)
        positions = {}
        for i, num in enumerate(nums):
            if num in positions.keys():
                positions[num].append(i)
            else:
                positions[num] = [i]

        nums = list(set(nums))
        merge_sort(nums)
        counter = 0
        for num in nums:
            for pos in positions[num]:
                result[pos] = counter
            counter += len(positions[num])

        return result


if __name__ == '__main__':
    nums = [8, 1, 2, 2, 3]
    s = Solution()
    print(f'Test 1: {s.smallerNumbersThanCurrent_fast(nums)}')
