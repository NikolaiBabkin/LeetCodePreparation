import unittest
import random
import heapq
from DS_Algorithms.sorting.my_sort import MySort
from DS_Algorithms.sorting.merge_sort import merge_sort
from DS_Algorithms.sorting.quick_sort import quicksort_iterative, quicksort_recursion
from DS_Algorithms.quick_select import quick_select_iterative, quick_select_recursion
from DS_Algorithms.median_of_median import median_of_median


class MySortTest(unittest.TestCase):
    def test_old_merge_sort(self):
        for _ in range(10):
            arr = [random.randint(1, 1000) for _ in range(1000)]
            self.assertEqual(MySort.merge_sort(arr, inplace=False), sorted(arr))

    def test_merge_sort(self):
        for _ in range(10):
            arr = [random.randint(1, 1000) for _ in range(1000)]
            self.assertEqual(merge_sort(arr, inplace=False), sorted(arr))

    def test_quicksort_iterative(self):
        for _ in range(10):
            arr = [random.randint(1, 1000) for _ in range(1000)]
            self.assertEqual(quicksort_iterative(arr), sorted(arr))

    def test_quicksort_recursion(self):
        for _ in range(10):
            arr = [random.randint(1, 1000) for _ in range(1000)]
            self.assertEqual(quicksort_recursion(arr), sorted(arr))

    def test_quick_select_recursion(self):
        for _ in range(10):
            arr = [random.randint(1, 1000) for _ in range(1000)]
            k = random.randint(1, 1000)
            self.assertEqual(quick_select_recursion(arr, k), heapq.nsmallest(k, arr)[-1])

    def test_quick_select_iterative(self):
        for _ in range(10):
            arr = [random.randint(1, 1000) for _ in range(1000)]
            k = random.randint(1, 1000)
            self.assertEqual(quick_select_iterative(arr, k), heapq.nsmallest(k, arr)[-1])

    def test_median_of_median(self):
        for _ in range(10):
            arr = [random.randint(1, 1000) for _ in range(1000)]
            k = random.randint(1, 1000)
            self.assertEqual(median_of_median(arr, k), heapq.nsmallest(k, arr)[-1])

    def test_heap_sort(self):
        pass
        # arr = list(range(100, 1, -1))
        # self.assertEqual(heap_sort(arr, inplace=False), sorted(arr))


if __name__ == '__main__':
    unittest.main()
