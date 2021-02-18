import heapq


class Solution:
    def findKthLargest_heap(self, arr, k):
        """
        Time Complexity: O(n)<= T <= O(log(n))
        Space Complexity: O(k)
        """
        return heapq.nlargest(k, arr)[-1]

    def findKthLargest_recursion(self, arr, k):
        """
        Time Complexity: O(n)
        Space Complexity: O(log(n))
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

        k = len(arr) - k + 1
        return kth_statistic(0, len(arr) - 1, k)

    def findKthLargest_iterative(self, arr, k):
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

        k = len(arr) - k + 1
        stack = [(0, len(arr) - 1)]
        while stack:
            lo, hi = stack.pop()
            if lo == hi:
                return arr[lo]
            p = partition(lo, hi)
            if k == p + 1:
                break
            if k - 1 < p:
                stack.append((lo, p - 1))
            if k - 1 > p:
                stack.append((p + 1, hi))

        return arr[p]


if __name__ == '__main__':
    s = Solution()
    arr = [1]
    k = 1
    print(s.findKthLargest_iterative(arr, k))