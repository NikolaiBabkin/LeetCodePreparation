import copy


def quicksort_recursion(array):
    def _qsort(lo, hi):
        if lo < hi:
            p = _partition(lo, hi)
            _qsort(lo, p - 1)
            _qsort(p + 1, hi)

    def _partition(lo, hi):
        mid = (lo + hi) // 2
        if arr[hi] < arr[lo]:
            arr[hi], arr[lo] = arr[lo], arr[hi]
        if arr[lo] < arr[mid] < arr[hi]:
            arr[mid], arr[hi] = arr[hi], arr[mid]
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

    arr = copy.deepcopy(array)
    _qsort(0, len(arr) - 1)
    return arr


def quicksort_iterative(array):
    def _partition(lo, hi):
        mid = (lo + hi) // 2
        if arr[hi] < arr[lo]:
            arr[hi], arr[lo] = arr[lo], arr[hi]
        if arr[lo] < arr[mid] < arr[hi]:
            arr[mid], arr[hi] = arr[hi], arr[mid]
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

    arr = copy.deepcopy(array)
    stack = [(0, len(arr) - 1)]
    while stack:
        lo, hi = stack.pop()
        if lo >= hi:
            continue
        p = _partition(lo, hi)
        stack.append((lo, p - 1))
        stack.append((p + 1, hi))

    return arr


if __name__ == '__main__':
    arr = [10] * 10000
    print(arr)
    res = quicksort_recursion(arr)
    print(arr)
    print(res)
