from DS_Algorithms.sorting.my_sort import MySort
from DS_Algorithms.sorting.merge_sort import merge_sort
from DS_Algorithms.sorting.heap_sort import heap_sort

if __name__ == '__main__':
    a = list(range(10, 0, -1))
    MySort.merge_sort(a)
    print(f'merge_sort_OLD result: {a}')

    a = list(range(10, 0, -1))
    merge_sort(a)
    print(f'merge_sort result: {a}')

    a = list(range(10, 0, -1))
    heap_sort(a)
    print(f'heap_sort result: {a}')
