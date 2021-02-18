import unittest
import random
from DS_Algorithms.sorting.my_sort import MySort
from DS_Algorithms.sorting.merge_sort import merge_sort
from DS_Algorithms.sorting.quick_sort import quicksort_iterative, quicksort_recursion


class MySortTest(unittest.TestCase):
    def test_old_merge_sort(self):
        arr = [random.randint(1, 1000) for _ in range(1000)]
        self.assertEqual(MySort.merge_sort(arr, inplace=False), sorted(arr))

    def test_merge_sort(self):
        arr = [random.randint(1, 1000) for _ in range(1000)]
        self.assertEqual(merge_sort(arr, inplace=False), sorted(arr))

    def test_quicksort_iterative(self):
        arr = [random.randint(1, 1000) for _ in range(1000)]
        self.assertEqual(quicksort_iterative(arr), sorted(arr))

    def test_quicksort_recursion(self):
        arr = [random.randint(1, 1000) for _ in range(1000)]
        self.assertEqual(quicksort_recursion(arr), sorted(arr))

    def test_heap_sort(self):
        pass
        # arr = list(range(100, 1, -1))
        # self.assertEqual(heap_sort(arr, inplace=False), sorted(arr))


if __name__ == '__main__':
    unittest.main()
