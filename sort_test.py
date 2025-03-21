# unit test for updown_sort

import unittest

from sort_timer import updown_sort

class TestSort(unittest.TestCase):
    def test_updown_sort(self):
        #data = [8564, 62296, 81562, 23658, 45323, 78247, 83829, 76408, 87461]

        data = [57733, 47474, 33893, 62684, 21200, 10722, 54591, 34511, 91722, 9023, 56476, 73120, 29644, 14380, 94256, 23634, 54590, 55343, 32431, 4019]
        copy = data[:]
        copy.sort()
        res = updown_sort(data)
        self.assertEqual(res, copy)