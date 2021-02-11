class ListNode(object):
    def __init__(self, val, key=None, prev=None, next=None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next


class PriorityLinkedList:
    def __init__(self, capacity):
        self._size = 0
        self.head = ListNode(val=0)
        self.tail = ListNode(val=0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.location = dict()

    def get(self, key):
        if key not in self.location:
            return -1
        node = self.location[key]
        self._update_priority(node)
        return node.val

    def _update_priority(self, node):
        self._delete_node(node)
        self._insert_at_tail(node)

    def _delete_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self._size -= 1

    def _insert_at_tail(self, node):
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
        self._size += 1
        self.location[node.key] = node

    def put(self, key, value):
        if key in self.location:
            node = self.location[key]
            node.val = value
            self._update_priority(node)
        else:
            if self._size == self.capacity:
                to_delete = self.head.next
                self._delete_node(to_delete)
                # delete key from location
                self.location.pop(to_delete.key)

            node = ListNode(val=value, key=key)
            self._insert_at_tail(node)


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = PriorityLinkedList(capacity)

    def get(self, key: int) -> int:
        return self.cache.get(key)

    def put(self, key: int, value: int) -> None:
        self.cache.put(key, value)


if __name__ == '__main__':
# Your LRUCache object will be instantiated and called as such:
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))
    cache.put(4, 4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))