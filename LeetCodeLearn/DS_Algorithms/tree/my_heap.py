__about__ = """Heap implementation"""

__all__ = ['heapify', 'heappush', 'heappop']


def heapify(arr):
    """
    :param arr: array to heapify
    :return: inplace rearrange array

    Transform list into a heap, in-place. Time complexity is log(len(arr)).
    Transform button-up. Each i-th element should satisfy:
    1. arr[i] <= arr[2*i + 1]
    and
    2. arr[i] <= arr[2*i + 2]
    It is not necessary to start from las one element since it doesn't have
    any children. We should start from element with at least left children,
    so 2 * i + 1 < n, i < (n - 1) / 2.
    If n is even, then n = 2 * j, i < (2 * j - 1) / 2 = j - 1 / 2.
    If n is odd, then n = 2 * j + 1, i < (2 * j + 1 - 1) / 2 = j.
    So i < n // 2
    """
    n = len(arr)
    for i in reversed(range(n // 2)):
        _siftdown(arr, i)


def _siftdown(arr, start):
    if start >= len(arr):
        raise IndexError('list index out of range')
    pos = start
    leftchild = 2 * pos + 1
    rightchild = 2 * pos + 2
    while leftchild < len(arr):
        if rightchild < len(arr):
            if arr[pos] > min(arr[leftchild], arr[rightchild]):
                if arr[leftchild] <= arr[rightchild]:
                    arr[pos], arr[leftchild] = arr[leftchild], arr[pos]
                    pos = leftchild
                else:
                    arr[pos], arr[rightchild] = arr[rightchild], arr[pos]
                    pos = rightchild

                leftchild = 2 * pos + 1
                rightchild = 2 * pos + 2

            else:
                break
        else:
            if arr[pos] > arr[leftchild]:
                arr[pos], arr[leftchild] = arr[leftchild], arr[pos]
            break


def _siftup(arr, start):
    if start >= len(arr):
        raise IndexError('list index out of range')
    pos = start
    parent = (pos - 1) // 2
    while parent >= 0:
        if arr[pos] < arr[parent]:
            arr[pos], arr[parent] = arr[parent], arr[pos]
            pos = parent
            parent = (pos - 1) // 2
        else:
            break


def heappush(heap, num):
    heap = heap.append(num)
    _siftup(heap, len(heap) - 1)


def heappop(heap):
    if heap:
        heap[0], heap[-1] = heap[-1], heap[0]
        res = heap.pop()
        if heap:
            _siftdown(heap, 0)
        return res
    else:
        raise IndexError('list is empty')


def nlargest(n, heap, key=None):
    # TODO: implement nlargest function
    pass


def nsmallest(n, iterable, key=None):
    # TODO: implement nsmallest function
    pass
