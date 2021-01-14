# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists_iterative(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Iterative solution
        Time Complexity: O(n+m)
        Space Complexity: O(n+m)
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val > l2.val:
            l1, l2 = l2, l1
        res = l1
        pointer_res = res
        pointer_1 = l1.next
        pointer_2 = l2
        while pointer_1 or pointer_2:
            if pointer_1 is None:
                pointer_res.next = pointer_2
                return res
            elif pointer_2 is None:
                pointer_res.next = pointer_1
                return res
            else:
                if pointer_1.val <= pointer_2.val:
                    pointer_res.next = pointer_1
                    pointer_1 = pointer_1.next
                else:
                    pointer_res.next = pointer_2
                    pointer_2 = pointer_2.next
                pointer_res = pointer_res.next
        return res

    def mergeTwoLists_recuesive(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Recursive solution
        Time Complexity: O(n+m)
        Space Complexity: O(n+m)
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists_recuesive(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists_recuesive(l1, l2.next)
        return l2

    def mergeTwoLists_iterative_sufficient(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Iterative sufficient solution
        Time Complexity: O(n+m)
        Space Complexity: O(1)
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val > l2.val:
            l1, l2 = l2, l1

        pointer_1 = l1
        pointer_2 = l2
        while True:
            while pointer_1.next and pointer_1.next.val <= pointer_2.val:
                pointer_1 = pointer_1.next
            if pointer_1.next is None:
                pointer_1.next = pointer_2
                break
            if pointer_1.next.val > pointer_2.val:
                pointer_1.next, pointer_2 = pointer_2, pointer_1.next
                pointer_1 = pointer_1.next

        return l1

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Iterative super cooooool solution
        Time Complexity: O(n+m)
        Space Complexity: O(1)
        """
        res = ListNode(-1)
        prev = res
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        prev.next = l1 if l2 is None else l2
        return res.next
