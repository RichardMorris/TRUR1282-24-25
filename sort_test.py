# unit test for updown_sort

import unittest

from sort_timer import *

class TestSort(unittest.TestCase):
    def test_updown_sort_simple(self):
        #data = [8564, 62296, 81562, 23658, 45323, 78247, 83829, 76408, 87461]

        data = [57733, 47474, 33893, 62684, 21200, 10722, 54591, 34511, 91722, 9023, 56476, 73120, 29644, 14380, 94256, 23634, 54590, 55343, 32431, 4019]
        copy = data[:]
        copy.sort()
        res = updown_sort(data, SimpleMerger())
        self.assertEqual(res, copy)

    def test_updown_sort_increaing_length_merger(self):
        data = [8564, 62296, 81562, 23658, 45323, 78247, 83829, 76408, 87461]

        #data = [57733, 47474, 33893, 62684, 21200, 10722, 54591, 34511, 91722, 9023, 56476, 73120, 29644, 14380, 94256, 23634, 54590, 55343, 32431, 4019]
        copy = data[:]
        copy.sort()
        res = updown_sort(data, IncreasingLengthMerger())
        self.assertEqual(res, copy)

    def test_updown_sort_tree_queue(self):
        data = [8564, 62296, 81562, 23658, 45323, 78247, 83829, 76408, 87461]

        #data = [57733, 47474, 33893, 62684, 21200, 10722, 54591, 34511, 91722, 9023, 56476, 73120, 29644, 14380, 94256, 23634, 54590, 55343, 32431, 4019]
        copy = data[:]
        copy.sort()
        res = updown_sort(data, TreeMerger())
        self.assertEqual(res, copy)

    def test_updown_sort_dequeue(self):
        data = [8564, 62296, 81562, 23658, 45323, 78247, 83829, 76408, 87461]

        #data = [57733, 47474, 33893, 62684, 21200, 10722, 54591, 34511, 91722, 9023, 56476, 73120, 29644, 14380, 94256, 23634, 54590, 55343, 32431, 4019]
        copy = data[:]
        copy.sort()
        res = updown_sort(data, DequeMerger())
        self.assertEqual(res, copy)

    def test_updown_sort_single_item_list_simple(self):
        data = [3]
        copy = data[:]
        copy.sort()
        res = updown_sort(data, SimpleMerger())
        self.assertEqual(res, copy)

    def test_updown_sort_single_item_list_increasing(self):
        # arrange
        data = [3]
        copy = data[:]
        copy.sort()

        # act
        res = updown_sort(data, IncreasingLengthMerger())

        #assert
        self.assertEqual(res, copy)

    def test_updown_sort_zero_item_list_simple(self):
        # arrange
        data = []
        copy = data[:]
        copy.sort()

        # act
        res = updown_sort(data, SimpleMerger())

        #assert
        self.assertEqual(res, copy)

    def test_updown_sort_single_item_list_tree(self):
        data = [3]
        copy = data[:]
        copy.sort()
        res = updown_sort(data, TreeMerger())
        self.assertEqual(res, copy)

    def test_updown_sort_zero_item_list_increasing(self):
        # arrange
        data = []
        copy = data[:]
        copy.sort()

        # act
        res = updown_sort(data, IncreasingLengthMerger())

        #assert
        self.assertEqual(res, copy)

    def test_updown_sort_zero_item_list_tree(self):
        data = []
        copy = data[:]
        copy.sort()
        res = updown_sort(data, TreeMerger())
        self.assertEqual(res, copy)
