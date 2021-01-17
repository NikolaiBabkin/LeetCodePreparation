from DS_Algorithms.tree import my_heap
import random

# TODO: implement Heap sort
# def _siftdown(arr, start, end=None):
#     if end is None:
#         end = len(arr)
#     if start >= end:
#         raise IndexError('list index out of range')
#     pos = start
#     leftchild = 2 * pos + 1
#     rightchild = 2 * pos + 2
#     while leftchild < end:
#         if rightchild < end:
#             if arr[pos] > min(arr[leftchild], arr[rightchild]):
#                 if arr[leftchild] <= arr[rightchild]:
#                     arr[pos], arr[leftchild] = arr[leftchild], arr[pos]
#                     pos = leftchild
#                 else:
#                     arr[pos], arr[rightchild] = arr[rightchild], arr[pos]
#                     pos = rightchild
#
#                 leftchild = 2 * pos + 1
#                 rightchild = 2 * pos + 2
#
#             else:
#                 break
#         else:
#             if arr[pos] > arr[leftchild]:
#                 arr[pos], arr[leftchild] = arr[leftchild], arr[pos]
#             break
#
#
# def heapify(arr):
#     n = len(arr)
#     for i in reversed(range(n // 2)):
#         _siftdown(arr, i)


def heap_sort(arr):
    my_heap.heapify(arr)
    res = []
    while arr:
        res.append(my_heap.heappop(arr))
    return res


if __name__ == '__main__':
    data_1 = []
    for i in range(10000):
        item = random.randint(-1000, 1000)
        data_1.append(item)

    res = heap_sort(data_1)
    print(res == sorted(res))