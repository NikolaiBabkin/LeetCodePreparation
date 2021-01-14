import unittest
from DS_Algorithms.sorting.my_sort import MySort
from DS_Algorithms.sorting.merge_sort import merge_sort
from DS_Algorithms.sorting.heap_sort import heap_sort


class MySortTest(unittest.TestCase):
    def test_old_merge_sort(self):
        arr = list(range(100, 1, -1))
        self.assertEqual(MySort.merge_sort(arr, inplace=False), sorted(arr))

    def test_merge_sort(self):
        arr = list(range(100, 1, -1))
        self.assertEqual(merge_sort(arr, inplace=False), sorted(arr))

    def test_heap_sort(self):
        pass
        # arr = list(range(100, 1, -1))
        # self.assertEqual(heap_sort(arr, inplace=False), sorted(arr))


if __name__ == '__main__':
    unittest.main()
