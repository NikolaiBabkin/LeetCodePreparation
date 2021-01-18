import collections
import heapq
import random


class Solution:
    def topKFrequent_1(self, nums, k):
        """
        Time Complexity: O(k*log(k))
        Space Complexity: O(n)
        """
        nums_cnt = collections.Counter(nums)
        comparator = lambda x: nums_cnt[x]
        return heapq.nlargest(k, nums_cnt, comparator)

    def topKFrequent_2(self, nums, k):
        """
        Time Complexity: O(k*log(k))
        Space Complexity: O(n)
        """
        return [i[0] for i in collections.Counter(nums).most_common(k)]

    def topKFrequent_3(self, nums, k):
        """
        Time Complexity: O(k*log(k))
        Space Complexity: O(n)
        """
        def heapify(arr):
            n = len(arr)
            for i in reversed(range(n // 2)):
                _sift_down(arr, i)

        def _sift_down(arr, k):
            n = len(arr)
            curr = k
            left = 2 * curr + 1
            right = 2 * curr + 2
            while left < n:
                if right < n:
                    if arr[curr] > min(arr[left], arr[right]):
                        if arr[left] <= arr[right]:
                            arr[curr], arr[left] = arr[left], arr[curr]
                            curr = left
                        else:
                            arr[curr], arr[right] = arr[right], arr[curr]
                            curr = right
                        left = 2 * curr + 1
                        right = 2 * curr + 2
                    else:
                        break
                else:
                    if arr[curr] > arr[left]:
                        arr[curr], arr[left] = arr[left], arr[curr]
                    break

        def heapreplace(heap, num):
            heap[0] = num
            _sift_down(heap, 0)

        def nlargest(n, arr):
            if n >= len(arr):
                return sorted(arr, reverse=True)

            # make min heap from k firs elements
            result = arr[:k]
            heapify(result)
            for num in arr[k:]:
                if num > result[0]:
                    # pop head and insert num
                    heapreplace(result, num)

            return sorted(result, reverse=True)

        nums_cnt = collections.Counter(nums)
        counts = [nums_cnt[key] for key in nums_cnt]
        kth = nlargest(k, counts)[-1]
        result = [key for key in nums_cnt if nums_cnt[key] >= kth]
        return result

    def topKFrequent_4(self, nums, k):
        def k_statistic(arr, k):
            n = len(arr)
            if n < 100:
                res = sorted(arr)[k]
                return res

            for i in range(n // 5):
                arr[5 * i: 5 * (i + 1)] = sorted(arr[5 * i: 5 * (i + 1)])

            split = k_statistic(arr[2::5], len(arr[2::5]) // 2 + 1)
            split_pos = sum(1 for i in arr if i <= split)
            if split_pos == n or split_pos == 0:
                split_pos = n // 2
                split = arr[split_pos]
            if k < split_pos:
                sub_array = [num for num in arr if num <= split]
                res = k_statistic(sub_array, k)
            elif k > split_pos:
                sub_array = [num for num in arr if num > split]
                res = k_statistic(sub_array, k - split_pos)
            else:
                res = split
            return res

        nums_cnt = collections.Counter(nums)
        counts = [nums_cnt[key] for key in nums_cnt]
        kth = k_statistic(counts, len(counts) - k + 1)
        return [key for key in nums_cnt if nums_cnt[key] >= kth]

    def topKFrequent_5(self, nums, k):
        bucket = [[] for _ in range(len(nums) + 1)]
        Count = collections.Counter(nums).items()
        for num, freq in Count: bucket[freq].append(num)
        flat_list = list(collections.chain(*bucket))
        return flat_list[::-1][:k]


if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    k = 2
    s = Solution()
    print(s.topKFrequent_5(nums, k))
    # data = list(reversed(range(1000)))
    # random.shuffle(data)
    # k = 900
    # print(f'k_statistic: {k_statistic(data, k)}')
    # print(f'true res: {data[k - 1]}')

