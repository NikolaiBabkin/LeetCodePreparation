class MyLinkedListNode(object):
    def __init__(self, val: int, prev=None, next=None):
        self.val = val
        self.prev = prev


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self._length = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list.
        If the index is invalid, return -1.
        """
        if 0 <= index < self._length:
            res = self.head
            for _ in range(index):
                res = res.next
            return res.val
        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        """
        node = MyLinkedListNode(val=val, next=self.head)
        self.head = node
        self._length += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.head:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = MyLinkedListNode(val=val)
        else:
            self.head = MyLinkedListNode(val=val)
        self._length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list,
        the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        """
        if index == self._length:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        elif 0 < index < self._length:
            cur = self.head
            for _ in range(index - 1):
                cur = cur.next
            node = MyLinkedListNode(val=val, next=cur.next)
            cur.next = node
            self._length += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index == 0:
            self.head = self.head.next
            self._length -= 1
        elif 0 < index < self._length:
            cur = self.head
            for _ in range(index - 1):
                cur = cur.next
            cur.next = cur.next.next
            self._length -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
