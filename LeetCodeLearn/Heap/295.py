from heapq import *


class MedianFinder:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def _reballance(self):
        while len(self.max_heap) > len(self.min_heap) + 1:
            num = - heappop(self.max_heap)
            heappush(self.min_heap, num)

        while len(self.min_heap) > len(self.max_heap) + 1:
            num = heappop(self.min_heap)
            heappush(self.max_heap, - num)

    def addNum(self, num: int) -> None:
        if self.min_heap and num >= self.min_heap[0]:
            heappush(self.min_heap, num)
        else:
            heappush(self.max_heap, - num)

        self._reballance()

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return - self.max_heap[0]
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]

        return (self.min_heap[0]- self.max_heap[0]) / 2


if __name__ == '__main__':
    s = MedianFinder()
    s.addNum(1)
    s.addNum(2)
    s.addNum(3)
    s.addNum(4)
    print(s.findMedian())