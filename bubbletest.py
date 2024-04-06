import unittest
from bubble import bubbleSort


class TestBubbleSort(unittest.TestCase):

    def test_types(self):
        self.assertRaises(TypeError, bubbleSort, False)
        self.assertRaises(TypeError, bubbleSort, 2j)
        self.assertRaises(TypeError, bubbleSort, 21)
        self.assertRaises(TypeError, bubbleSort, [4.3, 5.2])
        self.assertRaises(TypeError, bubbleSort, [1, 2, 3, 4, 5], 6)
        self.assertRaises(TypeError, bubbleSort, 'eight')
        self.assertRaises(TypeError, bubbleSort, ['Vasya', 1, 2, 3, 3j], 4, 35, 12)
        self.assertRaises(TypeError, bubbleSort, [[]])

    def test_sorted_array(self):
        arr = [2, -24, 13839, 273, -383, 82, 3, 2, 5]
        sorted_list = bubbleSort(arr)
        expected_sorted_list = [-383, -24, 2, 2, 3, 5, 82, 273, 13839]
        self.assertEqual(sorted_list, expected_sorted_list)

        print("Відсортований список:")
        for element in sorted_list:
            print(element, end=" ")


if __name__ == "__main__":
    unittest.main()
