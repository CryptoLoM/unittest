import unittest
import sys
import io
from bubble import bubbleSort
import bubble as b

class TestBubbleSort(unittest.TestCase):

    def test_succes(Askim):
        nums_exit_code_0 = [2, 3, 1, 2, 1, 3.1]
        exit_code_0 = b.main(nums_exit_code_0)[0]
        Askim.assertEqual(exit_code_0, 0)

    def test_succes_after_correction(self):
        nums_exit_code_1 = ['Evgeniy Vitaliyovych', 3, 1, 'sdmksb', 1, 3.1]
        exit_code_1 = b.main(nums_exit_code_1)  # Отримання коду виходу
        self.assertEqual(exit_code_1, 1)
        nums_exit_code_1_str = "1 1 3 3.1 "
        exit_code_1_str = b.main(nums_exit_code_1_str)  # Отримання коду виходу
        self.assertEqual(exit_code_1_str, 1)

    def test_failure(Sensei):
        nums_exit_code_2 = ['oh my cookish','ya','ni ne tu']
        exit_code_2 = b.fail(nums_exit_code_2)  # Отримання коду виходу
        Sensei.assertEqual(exit_code_2, 2)

    def test_empty(self):
        arr = []
        expected_arr = []
        self.assertEqual(bubbleSort(arr), expected_arr)


    def test_one_element(self):
        array = [21]
        expected_result = [21]
        self.assertEqual(bubbleSort(array), expected_result)


    def test_same_elements(self):
        massive = [3, 1, 3, 2, 3, 2]
        expected_massive = [1, 2, 2, 3, 3, 3]
        sort_massive = bubbleSort(massive)
        self.assertEqual(bubbleSort(massive), expected_massive)


    def test_float_elements(self):
        arr = [1.3, 12.2345,12.2346, 1.29, 34]
        expected_arr= [1.29, 1.3, 12.2345, 12.2346, 34]
        sorted_arr = bubbleSort(arr)
        self.assertEqual(bubbleSort(arr), expected_arr)


    def test_negative_elements(self):
        array = [-21, 123, -8, 2, -23]
        expected_res = [-23, -21, -8, 2, 123]
        self.assertEqual(bubbleSort(array), expected_res)


    def test_valid_array(self):
        arr = [24, 13839, 273, 383, 82, 3, 2, 5]
        sorted_list = bubbleSort(arr)
        expected_sorted_list = [2, 3, 5, 24, 82, 273, 383, 13839]
        self.assertEqual(sorted_list, expected_sorted_list)


    def test_not_full_valid_array(self):
        arr = ['kadgkh', 71347, 4673]
        sorted_array = bubbleSort(arr)
        expected = [4673, 71347]
        self.assertEqual(sorted_array, expected)


    def test_not_valid_array(self):
          self.assertRaises(TypeError,bubbleSort,[2j,'knjd'],'ncdn')


    def test_already_sorted_list(self):
        # Arrange
        sorted_list = [1, 2, 3, 4, 5]
        # Act
        result = bubbleSort(sorted_list)
        # Assert
        self.assertEqual(result, sorted_list)
        self.assertTrue(result == sorted_list, "The list remain the same, becasuse it's already sorted")

if __name__ == "__main__":
    unittest.main()
