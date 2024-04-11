import unittest
import subprocess
from bubble import bubbleSort


class TestBubbleSort(unittest.TestCase):

    def test_exit_code_success(self):
        # Arrange
        list = [1, 4, -4, 5]

        # Act
        exit_code = subprocess.call("bubble.py", shell=True)

        # Assert
        self.assertEqual(exit_code, 0)

    def test_exit_code_success_after_correction(self):
        # Arrange
        list1 = ['afsdg', 1.23, 2, -1]

        # Act
        exit_code = subprocess.call("bubble.py", shell=True)

        # Assert
        self.assertNotEqual(exit_code, 1)


    def test_exit_code_failure(self):
        # Arrange
        list3 = ['jfjshf','hgsdf', 'dnjd']

        # Act
        exit_code = subprocess.call("bubble.py", shell=True)

        # Assert
        self.assertNotEqual(exit_code, 2)


    def test_empty(self):
        arr = []
        expected_arr = []
        self.assertEqual(bubbleSort(arr), expected_arr)

    def test_one_element(self):
        array = [21]
        expected_result = [21]
        self.assertEqual(bubbleSort(array), expected_result)


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
