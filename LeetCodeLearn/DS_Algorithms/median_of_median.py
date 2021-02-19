import heapq
import random


def median_of_median(arr, k):
    def kth_statistic(lo, hi, k):
        while lo < hi:
            p_idx = partition(lo, hi, k)
            if k < p_idx + 1:
                hi = p_idx - 1
            elif k == p_idx + 1:
                return p_idx
            else:
                lo = p_idx + 1

        return lo

    def find_pivot(lo, hi):
        if hi - lo + 1 < 15:
            return hi
        for i in range(lo, hi + 1, 5):
            arr[lo: (lo + 5)] = sorted(arr[lo: (lo + 5)])

        swap_to = lo
        for i in range(lo + 2, hi, 5):
            arr[i], arr[swap_to] = arr[swap_to], arr[i]
            swap_to += 1
        sub_len = len(range(lo + 2, hi, 5))
        p_idx = kth_statistic(lo, lo + sub_len - 1, lo + sub_len // 2 + 1)
        return p_idx

    def partition(lo, hi, k):
        p_idx = find_pivot(lo, hi)
        arr[p_idx], arr[hi] = arr[hi], arr[p_idx]
        i = lo
        for j in range(lo, hi):
            if arr[j] < arr[hi]:
                arr[j], arr[i] = arr[i], arr[j]
                i += 1

        i_eq = i
        for j in range(i, hi):
            if arr[j] == arr[hi]:
                arr[i_eq], arr[j] = arr[j], arr[i_eq]
                i_eq += 1

        arr[i_eq], arr[hi] = arr[hi], arr[i_eq]

        if k < i + 1:
            return i
        if k <= i_eq + 1:
            return k - 1
        return i_eq

    k_idx = kth_statistic(0, len(arr) - 1, k)
    return arr[k_idx]


if __name__ == '__main__':
    # arr = [random.randint(1, 1000) for _ in range(5000)]
    arr = [10] * 10000
    k = random.randint(1, 1000)
    print(median_of_median(arr, k))
    print(heapq.nsmallest(k, arr)[-1])