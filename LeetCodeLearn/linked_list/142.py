# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if head is None or head.next is None:
            return None
        # is cycle in linked list
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if fast is None or fast.next is None:
            return None
        # calculate length of cycle
        cycle_length = 1
        fast = fast.next
        while fast != slow:
            fast = fast.next
            cycle_length += 1
        # find cycle start node
        slow = head
        fast = head
        for _ in range(cycle_length):
            fast = fast.next
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

