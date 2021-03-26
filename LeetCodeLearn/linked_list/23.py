import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __gt__(self, other):
        return self.val > other.val

    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return self.val == other.val


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        Time Complexity: O(N*log(k))
        Space Complexity: O(k)
        """
        k = len(lists)
        if k == 0:
            return None
        if k == 1:
            return lists[0]

        heap = []
        for i in range(k):
            if lists[i]:
                heap.append(lists[i])
        heapq.heapify(heap)

        res = ListNode()
        prev = res
        while heap:
            curr = heapq.heappop(heap)
            if curr.next:
                heapq.heappush(heap, curr.next)
            prev.next = curr
            prev = curr

        return res.next
