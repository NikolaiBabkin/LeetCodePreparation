class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = dict()
        for num in nums:
            if num in nums_count:
                nums_count[num] += 1
            else:
                nums_count[num] = 1

        heap = [-count for num, count in nums_count.items()]
        heapq.heapify(heap)
        for _ in range(k):
            kth_top = -heapq.heappop(heap)
        return [num for num, count in nums_count.items() if count >= kth_top]
