class ListNode(object):
    def __init__(self, x, prev=None, next=None):
        self.val = x
        self.prev = prev
        self.next = next


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._size = 0
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list.
        If the index is invalid, return -1.
        """
        if 0 <= index < self._size:
            if index <= self._size // 2:
                cur = self.head.next
                for _ in range(index):
                    cur = cur.next
            else:
                cur = self.tail.prev
                for _ in range(self._size - index - 1):
                    cur = cur.prev
            return cur.val

        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(index=0, val=val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(index=self._size, val=val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list,
        the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        """
        if 0 <= index <= self._size:
            if index <= self._size // 2:
                cur = self.head
                for _ in range(index):
                    cur = cur.next
                node = ListNode(val, next=cur.next, prev=cur)
                cur.next.prev = node
                cur.next = node
            else:
                cur = self.tail
                for _ in range(self._size - index):
                    cur = cur.prev
                node = ListNode(val, next=cur, prev=cur.prev)
                cur.prev.next = node
                cur.prev = node

            self._size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if 0 <= index < self._size:
            if index <= self._size // 2:
                cur = self.head
                for _ in range(index):
                    cur = cur.next
                cur.next = cur.next.next
                cur.next.prev = cur
            else:
                cur = self.tail
                for _ in range(self._size - index - 1):
                    cur = cur.prev
                cur.prev.prev.next = cur
                cur.prev = cur.prev.prev

            self._size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
