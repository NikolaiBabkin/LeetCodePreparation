from DS_Algorithms.tree import my_heap
import unittest
import random
import heapq

# TODO: write proper tests

def test_heapify():
    data_1 = []
    for i in range(100000):
        item = random.randint(-1000, 1000)
        data_1.append(item)
    data_2 = data_1.copy()
    my_heap.heapify(data_1)
    res = []
    while data_1:
        res.append(my_heap.heappop(data_1))

    return res == sorted(data_2)

# def test


if __name__ == '__main__':
    print(f'test_heapify: {test_heapify()}')