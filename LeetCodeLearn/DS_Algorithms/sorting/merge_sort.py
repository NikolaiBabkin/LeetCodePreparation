def merge_sort(arr, inplace=True, reverse=False):
    def _merge(left, mid, right):
        helper = [0] * (right - left)
        it1 = it2 = 0
        while (left + it1 < mid) & (mid + it2 < right):
            if arr[left + it1] <= arr[mid + it2]:
                helper[it1 + it2] = arr[left + it1]
                it1 += 1
            else:
                helper[it1 + it2] = arr[mid + it2]
                it2 += 1

        while left + it1 < mid:
            helper[it1 + it2] = arr[left + it1]
            it1 += 1

        while mid + it2 < right:
            helper[it1 + it2] = arr[mid + it2]
            it2 += 1

        arr[left:right] = helper

    def _merge_sort(left, right):
        if left + 1 < right:
            mid = int((left + right) / 2)
            _merge_sort(left, mid)
            _merge_sort(mid, right)
            _merge(left, mid, right)

    if not inplace:
        arr = arr.copy()
        _merge_sort(0, len(arr))
        if reverse:
            arr = arr[::-1]
        return arr

    _merge_sort(0, len(arr))
    if reverse:
        arr = arr[::-1]
