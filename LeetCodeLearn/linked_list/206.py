# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList_iterative(self, head: ListNode) -> ListNode:
        """
        Iterative approach
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if head and head.next:
            curr = head
            prev = None
            while curr:
                next_tmp = curr.next
                curr.next = prev
                prev = curr
                curr = next_tmp
            return prev
        return head


    def reverseList_recursive(self, head: ListNode) -> ListNode:
        """
        Recursive approach
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if (head is None) or (head.next is None):
            return head

        res_head = self.reverseList_recursive(head.next)
        head.next.next = head
        head.next = None
        return res_head



def make_example(arr):
    head = ListNode(arr[0])
    node = head
    for itm in arr[1:]:
        node.next = ListNode(itm)
        node = node.next
    return head


def print_linked_list(head):
    node = head
    while node:
        print(node.val)
        node = node.next


if __name__ == '__main__':
    s = Solution()
    arr = [1, 2, 3, 4, 5]
    head = make_example(arr)
    # new_head = s.reverseList_iterative(head)
    new_head = s.reverseList_recursive(head)
    print_linked_list(new_head)
