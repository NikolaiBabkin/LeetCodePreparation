class DoubleLinkedList:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class FirstUnique:
    def __init__(self, nums):
        self.head = DoubleLinkedList(-1)
        self.tail = self.head
        self.num_pointers = dict()
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        if self.tail.val == -1:
            return -1

        return self.head.next.val

    def add(self, value: int) -> None:
        if value in self.num_pointers:
            if isinstance(self.num_pointers[value], DoubleLinkedList):
                node = self.num_pointers[value]
                node.prev.next = node.next
                if node.val == self.tail.val:
                    self.tail = node.prev
                else:
                    node.next.prev = node.prev
                self.num_pointers[value] = -1
        else:
            self.tail.next = DoubleLinkedList(value, self.tail)
            self.tail = self.tail.next
            self.num_pointers[value] = self.tail


class FirstUnique2:
    def __init__(self, nums):
        self.unique = dict()
        self.values = set()
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        for k in self.unique:
            return k
        return -1

    def add(self, value: int) -> None:
        if value in self.values:
            self.unique.pop(value, 1)
        else:
            self.unique[value] = 1
            self.values.add(value)



if __name__ == '__main__':
    nums = [2,3,5]
    obj = FirstUnique2(nums)
    param_1 = obj.showFirstUnique()
    print(param_1)
    obj.add(5)
    param_2 = obj.showFirstUnique()
    print(param_2)
    obj.add(2)
    param_3 = obj.showFirstUnique()
    print(param_3)
    obj.add(3)
    param_4 = obj.showFirstUnique()
    print(param_4)