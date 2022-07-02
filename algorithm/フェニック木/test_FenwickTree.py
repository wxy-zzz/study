import unittest
from FenwickTree import FenwickTree

class TestFenwickTree(unittest.TestCase):

    def test_size_when_size_is_0(self):
        size = 0
        with self.assertRaises(ValueError):
            ft = FenwickTree(size)

    def test_size_when_size_is_1(self):
        size = 1
        ft = FenwickTree(size)
        self.assertEqual(ft.size, size)

    def test_size_when_size_is_2(self):
        size = 2
        ft = FenwickTree(size)
        self.assertEqual(ft.size, size)

    def test_data_when_size_is_1(self):
        size = 1
        ft = FenwickTree(size)
        self.assertEqual(ft.data, [0] * size)

    def test_data_when_size_is_2(self):
        size = 2
        ft = FenwickTree(size)
        self.assertEqual(ft.data, [0] * size)

    def test_add(self):
        ft = FenwickTree(1)
        self.assertEqual(ft.data, [0])
        ft.add(0, 2)
        self.assertEqual(ft.data, [2])
        ft.add(0, 4)
        self.assertEqual(ft.data, [6])

    def test_add_when_index_error(self):
        ft = FenwickTree(2)
        with self.assertRaises(IndexError):
            ft.add(-1, 1)
        ft.add(0, 1)
        ft.add(1, 1)
        with self.assertRaises(IndexError):
            ft.add(2, 1)

    def test_update(self):
        ft = FenwickTree(1)
        self.assertEqual(ft.data, [0])
        ft.update(0, 2)
        self.assertEqual(ft.data, [2])
        ft.update(0, 4)
        self.assertEqual(ft.data, [4])

    def test_update_when_index_error(self):
        ft = FenwickTree(2)
        with self.assertRaises(IndexError):
            ft.update(-1, 1)
        ft.update(0, 1)
        ft.update(1, 1)
        with self.assertRaises(IndexError):
            ft.update(2, 1)

    def test_sum(self):
        ft = FenwickTree(32)
        for i in range(32):  # [1,2,3,...] に設定
            ft.add(i, i+1)
        self.assertEqual(ft.sum(0,0), 0)
        self.assertEqual(ft.sum(0,1), 1)
        self.assertEqual(ft.sum(0,16), 136)
        self.assertEqual(ft.sum(0,32), 528)
        self.assertEqual(ft.sum(1,1), 0)
        self.assertEqual(ft.sum(8,16), 100)
        self.assertEqual(ft.sum(16,32), 392)

        for i in range(32):  # [2,4,6,...] に設定
            ft.add(i, i+1)
        self.assertEqual(ft.sum(0,0), 0)
        self.assertEqual(ft.sum(0,1), 2)
        self.assertEqual(ft.sum(0,16), 272)
        self.assertEqual(ft.sum(0,32), 1056)
        self.assertEqual(ft.sum(1,1), 0)
        self.assertEqual(ft.sum(8,16), 200)
        self.assertEqual(ft.sum(16,32), 784)

        for i in range(32):  # 再度 [1,2,3,...] に設定
            ft.update(i, i+1)
        self.assertEqual(ft.sum(0,0), 0)
        self.assertEqual(ft.sum(0,1), 1)
        self.assertEqual(ft.sum(0,16), 136)
        self.assertEqual(ft.sum(0,32), 528)
        self.assertEqual(ft.sum(1,1), 0)
        self.assertEqual(ft.sum(8,16), 100)
        self.assertEqual(ft.sum(16,32), 392)

    def test_sum_when_index_error(self):
        ft = FenwickTree(32)
        with self.assertRaises(IndexError):
            ft.sum(-1, 16)
        with self.assertRaises(IndexError):
            ft.sum(31, 1)
        with self.assertRaises(IndexError):
            ft.sum(16, 33)

if __name__ == "__main__":
    unittest.main()
