# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        node.val = node.next.val
        node.next = node.next.next