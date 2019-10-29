'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''

import math
from typing import List


class Solution:
    def findMedianSortedArray(self, nums: List[int]) -> float:
        length = len(nums)
        if len(nums) % 2 == 0:
            return (nums[int(length / 2)] + nums[int((length / 2)) - 1]) / 2
        else:
            return nums[int(math.floor(length / 2))]

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        The key idea is to divide nums1 and nums2 in such a way that the number of elements
        in the left partition is equal to the number of elements in the right partition
        In addition to that, the max element in the left partition should be less than the
        mininum element in the right partition

        :param nums1:
        :param nums2:
        :return:
        '''

        m = len(nums1)
        n = len(nums2)

        if m == 0:
            return self.findMedianSortedArray(nums2)

        if n == 0:
            return self.findMedianSortedArray(nums1)

        # Keep nums1 as the list with the lesser number of elements
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m

        # Possible range for the value of index (i) of partition of nums1
        i_min = 0
        i_max = m
        half_len = int((m + n + 1) / 2)

        while i_min <= i_max:
            # Set i to avg of the range(i_min, i_max)
            i = int((i_min + i_max + 1) / 2)

            # As the left partition and right partition should have equal number of elements,
            # j will be set to whatever's the difference left between half_len and i
            j = half_len - i

            max_val_in_left_partition = 0
            min_val_in_right_partition = 0

            # If the left partition of nums1 is empty, max val in left partition is the last element of the
            # nums2 left partition
            if i == 0:
                max_val_in_left_partition = nums2[j - 1]

            # If the left partition of nums2 is empty, max val in left partition is the last element of the
            # nums1 left partition
            if j == 0:
                max_val_in_left_partition = nums1[i - 1]

            # If the right partition of nums1 is empty, min val in right partition is the first element of the
            # nums1 right partition
            if i == m:
                min_val_in_right_partition = nums2[j]

            # If the right partition of nums2 is empty, min val in right partition is the first element of the
            # nums2 right partition
            if j == n:
                min_val_in_right_partition = nums1[i]

            # When both the left partitions are non-empty
            if i > 0 and j > 0:
                max_val_in_left_partition = max(nums1[i - 1], nums2[j - 1])

            # When both the right partitions are non-empty
            if i < m and j < n:
                min_val_in_right_partition = min(nums1[i], nums2[j])

            if max_val_in_left_partition <= min_val_in_right_partition:
                # We have arrived at the correct value of i and j
                # Now, we find the median

                if (m + n) % 2 == 0:
                    # Even length array
                    # Take average of the 2 values
                    return (max_val_in_left_partition + min_val_in_right_partition) / 2
                else:
                    # Odd length array
                    # Return just the value in the left partition
                    return max_val_in_left_partition

            if i > 0 and j < n and nums1[i - 1] > nums2[j]:
                # nums1 has too many elements in the left partition
                # Value of i has to be decreased
                i_max = i - 1

            if i < m and j > 0 and nums2[j - 1] > nums1[i]:
                # nums1 has too few elements in the left partition
                # Value of i has to be increased
                i_min = i

        return -1


import unittest


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test1(self):
        nums1 = [1, 3]
        nums2 = [2]
        self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), 2)

    def test2(self):
        nums1 = [1, 3]
        nums2 = [2, 4]
        self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), 2.5)

    def test3(self):
        nums1 = [1, 3, 5, 8, 9]
        nums2 = [2, 4, 6, 7, 13, 14]
        self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), 6)

    def test4(self):
        nums1 = [1, 3, 5, 7, 9]
        nums2 = [2, 4, 8, 9, 13, 14]
        self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), 7)

    def test5(self):
        nums1 = [1, 2, 3, 4]
        nums2 = [5, 6, 7, 8, 9]
        self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), 5)

    def test6(self):
        nums1 = [1, 2, 3, 4, 5]
        nums2 = [5, 6, 7, 8, 9]
        self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), 5)

    def test7(self):
        nums1 = [1, 2, 3, 4, 5]
        nums2 = [5, 6, 7]
        self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), 4.5)

    def test8(self):
        nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        nums2 = [5, 6, 7]
        self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), 5.5)

    def test9(self):
        nums1 = []
        nums2 = [5, 6, 7, 8]
        self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), 6.5)

    def test10(self):
        nums1 = []
        nums2 = [5, 6, 7]
        self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), 6)

    def test11(self):
        nums1 = [3]
        nums2 = [-2, -1]
        self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), -1)

    def test12(self):
        nums1 = [1, 2]
        nums2 = [3, 4]
        self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), 2.5)

    def test13(self):
        nums1 = []
        nums2 = [2]
        self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), 2)


if __name__ == "__main__":
    unittest.main()
