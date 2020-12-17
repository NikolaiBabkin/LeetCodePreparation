# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
class ImmutableListNode:
    def printValue(self) -> None: # print the value of this node.
    def getNext(self) -> 'ImmutableListNode': # return the next node.


class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        res = []
        node = head
        while node:
            res.append(node)
            node = node.getNext()
        while res:
            node = res.pop(-1)
            node.printValue()


    def print_linked_list_2(self, head: 'ImmutableListNode') -> None:
        """
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        node = head
        last_node = None
        while True:
            if node.getNext() == last_node:
                node.printValue()
                if node == head:
                    break
                last_node = node
                node = head
            else:
                node = node.getNext()

    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        """
        Time Complexity: O(n)
        Space Complexity: O(n^(1/2))
        """

        def helper(head: 'ImmutableListNode', stop_node) -> None:
            """
            Time Complexity: O(n)
            Space Complexity: O(n)
            """
            res = []
            node = head
            while node != stop_node:
                res.append(node)
                node = node.getNext()
            while res:
                node = res.pop(-1)
                node.printValue()

        size = 0
        node = head
        while node:
            size += 1
            node = node.getNext()

        step = int(size ** 0.5)
        sub_heads = [0] * (step)
        sub_heads[0] = head
        for i in range(1, len(sub_heads)):
            node = sub_heads[i - 1]
            cnt = step
            while cnt:
                if node.getNext():
                    node = node.getNext()
                    cnt -= 1
                else:
                    break
            if cnt == 0:
                sub_heads[i] = node

        stop_node = None
        for node in sub_heads[::-1]:
            helper(node, stop_node)
            stop_node = node


