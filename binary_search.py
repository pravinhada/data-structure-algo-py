import unittest


# binary search O(log n)
def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


class BinarySearchTest(unittest.TestCase):

    def test_binary_search(self):
        my_list = [1, 3, 4, 6, 7, 8, 9]
        self.assertEqual(binary_search(my_list, 7), 4)


if __name__ == '__main__':
    unittest.main()
