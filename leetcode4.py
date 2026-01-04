import unittest

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        # we are running the search on the lesser array (optimization)

        m = len(nums1)
        n = len(nums2)
        low = 0
        high = m

        while low <= high: #binary search for the median partitons
            partition1 = (low + high) // 2
            partition2 = ((m + n + 1) // 2) - partition1

            if partition1 > 0:
                maxleft1 = nums1[partition1 - 1]
            else:
                maxleft1 = float('-inf')

            if partition1 < m:
                minright1 = nums1[partition1]
            else:
                minright1 = float('inf')

            if partition2 > 0:
                maxleft2 = nums2[partition2 - 1]
            else:
                maxleft2 = float('-inf')

            if partition2 < n:
                minright2 = nums2[partition2]
            else:
                minright2 = float('inf')

            if maxleft1 <= minright2 and maxleft2 <= minright1: # partition checks
                if (m + n) % 2 == 1:
                    return float(max(maxleft1, maxleft2))
                else:
                    return (max(maxleft1, maxleft2) + min(minright1, minright2)) / 2.0

            elif maxleft1 > minright2:
                high = partition1 - 1
            else:
                low = partition1 + 1


class TestMedianFinder(unittest.TestCase): #unit tests
    def setUp(self):
        self.sol = Solution()

    def test_even_total_length(self):
        # (1 + 2 + 3 + 4) / 4 -> median of [1, 2, 3, 4] is (2 + 3) / 2 = 2.5
        self.assertEqual(self.sol.findMedianSortedArrays([1, 3], [2, 4]), 2.5)

    def test_odd_total_length(self):
        # [1, 2, 3] -> median is 2
        self.assertEqual(self.sol.findMedianSortedArrays([1, 3], [2]), 2.0)

    def test_one_empty_list(self):
        # [0, 0] -> median is 0
        self.assertEqual(self.sol.findMedianSortedArrays([], [0, 0]), 0.0)
        # [1] -> median is 1
        self.assertEqual(self.sol.findMedianSortedArrays([1], []), 1.0)

    def test_negative_numbers(self):
        # [-5, -3, 1, 4] -> median is (-3 + 1) / 2 = -1.0
        self.assertEqual(self.sol.findMedianSortedArrays([-5, 1], [-3, 4]), -1.0)

    def test_different_lengths(self):
        # [1, 2, 3, 4, 5, 6, 7] -> median is 4
        self.assertEqual(self.sol.findMedianSortedArrays([1, 2], [3, 4, 5, 6, 7]), 4.0)

if __name__ == '__main__':
    unittest.main()
