# import heapq
#
# def findKthLargest_heap(self, arr, k):
#     """
#     Time Complexity: O(n)
#     Space Complexity: O(1)
#     """
#     return heapq.nlargest(k, arr)[-1]

def quick_select_recursion(arr, k):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    def kth_statistic(lo, hi, k):
        if lo == hi:
            return arr[lo]
        p = partition(lo, hi)
        if k - 1 == p:
            return arr[p]
        if k - 1 < p:
            return kth_statistic(lo, p - 1, k)
        return kth_statistic(p + 1, hi, k)

    def partition(lo, hi):
        mid = (lo + hi) // 2
        if arr[lo] > arr[hi]:
            arr[lo], arr[hi] = arr[hi], arr[lo]
        if arr[lo] < arr[mid] < arr[hi]:
            arr[hi], arr[mid] = arr[mid], arr[hi]
        elif arr[mid] < arr[lo]:
            arr[hi], arr[lo] = arr[lo], arr[hi]

        pivot = arr[hi]

        i = lo
        for j in range(lo, hi):
            if arr[j] < pivot:
                arr[j], arr[i] = arr[i], arr[j]
                i += 1
        arr[i], arr[hi] = arr[hi], arr[i]
        return i

    return kth_statistic(0, len(arr) - 1, k)


def quick_select_iterative(arr, k):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    def partition(lo, hi):
        mid = (lo + hi) // 2
        if arr[lo] > arr[hi]:
            arr[lo], arr[hi] = arr[hi], arr[lo]
        if arr[lo] < arr[mid] < arr[hi]:
            arr[hi], arr[mid] = arr[mid], arr[hi]
        elif arr[mid] < arr[lo]:
            arr[hi], arr[lo] = arr[lo], arr[hi]

        pivot = arr[hi]

        i = lo
        for j in range(lo, hi):
            if arr[j] < pivot:
                arr[j], arr[i] = arr[i], arr[j]
                i += 1
        arr[i], arr[hi] = arr[hi], arr[i]
        return i

    lo, hi = (0, len(arr) - 1)
    while lo != hi:
        p = partition(lo, hi)
        if k == p + 1:
            return arr[p]
        if k - 1 < p:
            hi = p - 1
        if k - 1 > p:
            lo = p + 1

    return arr[lo]


if __name__ == '__main__':
    arr = [3,2,1,5,6,4]
    k = 2
    print(quick_select_recursion(arr, k))