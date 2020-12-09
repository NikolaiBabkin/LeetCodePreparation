import unittest
from DS_Algorithms.Sorting.my_sort import MySort


class MySortTest(unittest.TestCase):
    def test_merge_sort(self):
        arr = list(range(100, 1, -1))
        self.assertEqual(MySort.merge_sort(arr, inplace=False), sorted(arr))


if __name__ == '__main__':
    unittest.main()
