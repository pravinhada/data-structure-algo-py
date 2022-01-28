import unittest

# this doesn't work


def pair_sum1(list, sum):
    count = 0

    for i in range(len(list)-1):
        for j in range(i + 1, len(list)):
            if (list[i] + list[j]) == sum:
                print(list[i], list[j])
                count += 1

    return count


def pair_sum2(arr, k):
    if len(arr) < 2:
        return

    # set for tracking
    seen = set()
    output = set()

    for num in arr:

        target = k-num

        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target), max(num, target)))

    return len(output)


class PairTest(unittest.TestCase):

    def test_array_pair(self):
        self.assertEqual(pair_sum2([1, 3, 2, 2], 4), 2)
        self.assertEqual(pair_sum2([1, 2, 3, 1], 3), 1)
        self.assertEqual(pair_sum2(
            [1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10), 6)


if __name__ == '__main__':
    unittest.main()
