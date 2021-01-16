__about__ = """Heap implementation"""

__all__ = ['heapify', 'heappush', 'heappop']


class Heap(object):
    def __init__(self, arr=None):
        if arr:
            self.heap = self.heapify(arr)
        else:
            self.heap = []

    def heapify(self, arr):
        pass



def extract_min(heap):
    pass


def heappush(heap, num):
    pass


def heappop(heap):
    pass


def _siftup(heap, start):
    pass


def siftdown(heap, start):
    pass

